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
        },
        "apply_before": {
            "tag": "p",
            "kwargs": {
                "class": "text-primary mb-0",
            },
            "attrs": {
                "data-toggle": "tooltip"
            },
            "multi": False,
            "func": lambda a: a.split(":")[-1]
        },
        "details": {
            "tag": "h1",
            "kwargs": {
                "class": "text-primary font-weight-bold media-heading h4"
            },
            "multi": False,
            "nested": {
                "tag": "a",
                "kwargs": {
                    "class": ""
                },
                "multi": False,
                "url" : "https://merojob.com",
                "link": True,
            }
        }
    },
    "kumarijob": {
        "title": {
            "tag": "span",
            "kwargs": {
                "class": "title"
            },
            "multi": False
        },
        "org": {
            "tag": "span",
            "kwargs": {
                "class": "meta"
            },
            "multi": False
        },
        "details": {
            "tag": "a",
            "kwargs": {
                "class": "l__button l__button--lightblue float-end"
            },
            "multi": False,
            "link": True
        },
        "others": {
            "multi": True,
            "tag": "ul",
            "kwargs": {
                "class": "description__two"
            },
            "innerTag": "li",
            "innerKwargs": {

            },
        },
    },
    "slicejob": {
        "title": {
            "tag": "li",
            "kwargs": {
                "class": re.compile("job_tit(t)?tle")
            },
            "multi": False
        },
        "location": {
            "tag": "li",
            "kwargs": {
                "class": "job_company"
            },
            "multi": False
        },
        "posted_on": {
            "tag": "li",
            "kwargs": {
                "class": "job_postdate"
            },
            "multi": False
        },
        "details" : {
            "tag" : "div",
            "kwargs" : {
                "class" : "col-xs-12 col-md-2"
                },

            "nested" : {
                "tag" : "a",
                "kwargs" : {
                    "class" : "btn btn-view-detail col-xs-6 col-sm-12"
                    },
                "link" : True
                }
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
        "obj": {}
    },
    "slicejob": {
        "tag": "div",
        "kwargs": {
            "id": "item_list"
        },
        "obj": {}
    }
}
urls = ["https://www.merojob.com/search/?q=",
        "https://www.kumarijob.com/search?keywords=",
        "https://www.slicejob.com/jobs/search/?job_category=&submit=Search&job_tittle="
        ]
