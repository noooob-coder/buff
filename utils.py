import csv
import random
import requests
def cookie():
    f = open('data/cookie.txt', 'r')
    cookie = f.read()
    f.close()
    return cookie
def ua():
    f = open('data/ua.csv')
    ua_csv = csv.DictReader(f)
    ua = []
    for k in ua_csv:
        ua.append(k['ua'])
    f.close()
    return ua[random.randint(0, len(ua))]
def ip_get():
    api='请填写自己申请到的api接口'
    headers = {
        'User-Agent': ua(),
    }
    r=requests.get(url=api,headers=headers)
    return r.text