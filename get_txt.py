import requests
import utils
import random
import time
import utils
class Get_text(object):
    def __init__(self):
        ip=utils.ip_get().replace('\n','').replace('\r','')
        self.proxies = {'http': ip,
                        'https': ip
                        }
        print(ip)
        cookie=utils.cookie()
        self.cookies = {}
        self.headers = {
            'User-Agent': utils.ua(),
        }
        for line in cookie.split(';'):
            key, value = line.split('=', 1)
            self.cookies[key] = value
    def rst(self,url):
        try:
            r = requests.get(url=url, headers=self.headers, cookies=self.cookies,proxies=self.proxies)
        except:
            ip=utils.ip_get()
            self.proxies={
                'http': ip,
                'https': ip
            }
            r = requests.get(url=url, headers=self.headers, cookies=self.cookies, proxies=self.proxies)
        time.sleep(random.uniform(5, 10))
        return r.text



