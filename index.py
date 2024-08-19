from bs4 import BeautifulSoup
import requests
import json
import re

parseDataConfig = {
    "merojob": {
        "title": {
            "tag": "h1",
            "kwargs": {
                "itemprop": "title"
            },
            "multi": False

        },
        "org": {
            "tag": "h3",
            "kwargs": {
                "class": "h6"
            },
            "multi": False

        },
        "skills": {
            "multi": True,
            "tag": "span",
            "kwargs": {
                "itemprop": "skills"
            },
            "innerTag": "span",
            "innerKwargs": {

            },
        },
        "viewed_by": {
            "tag": "span",
            "kwargs": {
                "class": "text-primary"
            },
            "multi": False,
            "func": lambda a: a.split()[-1]
        }
    },
    "kumarijob": {
        "title": {
            "tag": "span",
            "kwargs": {
                "class": "title"
            },
            "multi": False
        }
    }
}

jobDataConfig = {
    "kumarijob": {
        "tag": "div",
        "kwargs": {
        },
        "obj": {
            "data-aos": "fade-up"
        }
    },
    "merojob": {
        "tag": "div",
        "kwargs": {
            "class": "card",
            "itemscope": "",
            "itemtype": "http://schema.org/JobPosting"
        },
        "obj": {

        }
    }
}

keys = ["react", "python", "frontend"]
# htmls = [""]
urls = ["https://www.merojob.com/search/?q=",
        "https://www.kumarijob.com/search?keywords="]
datas = list(map(lambda a: list(map(lambda b: b+a, urls)), keys))
datas = [{"url": a, "key": re.search(
    r"\.[a-zA-Z]*\.", a).group().replace(".", "")} for b in datas for a in b]
job_data_json_list = []
count = 1
for data in datas:
    soup = BeautifulSoup(requests.get(data["url"]).text, "lxml")
    jobs = soup.find_all(jobDataConfig[data["key"]]["tag"],
                         jobDataConfig[data["key"]]["obj"], **jobDataConfig[data["key"]]["kwargs"])
    for job in jobs:
        print(f"found {count} job(s)")
        count+=1
        for k, v in parseDataConfig.items():
            if data["url"].lower().find(k) != -1:
                job_data_json = {}
                for kk, vv in v.items():
                    if not vv["multi"]:
                        val = job.find(vv["tag"], **vv["kwargs"]).text
                        if "func" in vv:
                            val = vv["func"](val)
                        # print(kk, val.strip(), sep=":", end="\n")
                        job_data_json[kk] = val.strip()
                    else:
                        val = job.find(vv["tag"], **vv["kwargs"])
                        if val is not None:
                            # print(f"{kk}:", end="")
                            # print(*map(lambda a: a.text.strip(),
                            #       val.find_all(vv["innerTag"], **vv["innerKwargs"])), sep=",")
                            job_data_json[kk] = list(map(lambda a: a.text.strip(
                            ), val.find_all(vv["innerTag"], **vv["innerKwargs"])))
                # print("\n")
                job_data_json_list.append(job_data_json)
                break
        # job_org = job.find("h3",class_="h6")

        # job_medias = job.find_all("div",class_="media")[-1].find("div",class_="media-body").find("span",itemprop="skills")

        # job_title = job_title.text.strip()
        # job_org =job_org.text.strip()

        # print("Title",job_title,sep=":")
        # print("Org.",job_org,sep=":")
        # print("Skills:",end="")
        # if job_medias is not None:
        #     job_medias = filter(lambda a : len(a.strip())!=0,job_medias.text.split("\n"))
        #     print(*job_medias,sep=",",end="\n\n")

    # print("\n\n")

with open("data.json", "w") as f:
    f.write(json.dumps(job_data_json_list))
    f.close()
print("Data has been stored in data.json")
