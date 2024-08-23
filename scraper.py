import re
from bs4 import BeautifulSoup
import requests
from requests.exceptions import HTTPError
from bs4.element import Tag
import logger
from logger import log
from config import parseDataConfig,jobDataConfig,urls


def scrape(keys):
    def gen_nested(elem, vv):
        attrs = {}
        if "attrs" in vv:
            attrs = vv["attrs"]
        val = elem.find(vv["tag"], attrs, **vv["kwargs"])
        if val is None:
            return None
        if "link" in vv and vv["link"]:
            val = (vv["url"] if "url" in vv else "") + val["href"]
        if "func" in vv:
            val = vv["func"](val.text)
        if "nested" in vv:
            val = gen_nested(val, vv["nested"])
        return val

    def get_json_data(v):
        job_data_json = {}
        for kk, vv in v.items():
            if not vv["multi"]:
                val = gen_nested(job, vv)
                if val is None:
                    continue
                if isinstance(val, Tag):
                    val = val.text.strip()
                job_data_json[kk] = val
            else:
                val = job.find(vv["tag"], **vv["kwargs"])
                if val is not None:
                    job_data_json[kk] = list(map(lambda a: a.text.strip(
                    ), val.find_all(vv["innerTag"], **vv["innerKwargs"])))
        return job_data_json

    keys = keys.split()
    datas = list(map(lambda a: list(map(lambda b: b+a, urls)), keys))
    datas = [{"url": a, "key": (re.search(
        r"[^/www](\.)?[a-zA-Z]*\.", a) or "").group().replace(".", "")} for b in datas for a in b]

    job_data_json_list = []
    count = 1
    for data in datas:
        try:
            response = requests.get(data["url"], timeout=60)
            response.raise_for_status()
        except HTTPError as http_err:
            log(logger.Type.ERROR, f"{http_err}")
            continue
        except Exception as err:
            log(logger.Type.ERROR, f"{err}")
            continue

        if not data["key"]:
            log(logger.Type.ERROR, f"invalid key {data['key']}")
            continue

        if data["key"] not in jobDataConfig:
            log(logger.Type.ERROR,
                f"Configuration for key {data['key']} does not exist")
            continue
        soup = BeautifulSoup(response.text, "lxml")

        jobs = soup.find_all(jobDataConfig[data["key"]]["tag"],
                             jobDataConfig[data["key"]]["obj"], **jobDataConfig[data["key"]]["kwargs"])
        for job in jobs:
            print(f"found {count} job(s)")
            count += 1
            for k, v in parseDataConfig.items():
                if data["url"].lower().find(k) != -1:
                    job_data_json = get_json_data(v)
                    job_data_json_list.append(job_data_json)
                    break
    return job_data_json_list
