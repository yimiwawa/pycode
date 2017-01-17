__author__ = 'xinhua'

import requests

yue = ["01","02","03","04","05","06","07","08","09","10","11","12"]
ri = ["01","02","03","04","05","06","07","08","09","10",
      "11","12","13","14","15","16","17","18","19","20",
      "21","22","23","24","25","26","27","28","29","30","31"]

for i in yue:
    for j in ri:
        riqi = "2016" + i + j
        url = "http://103.37.161.139:8072/lafnews/2016/news." + riqi + ".tar.gz"
        print url
        r = requests.get(url)
        with open(riqi + ".tar.gz", "wb") as code:
            code.write(r.content)