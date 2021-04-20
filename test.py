import random
import time
import requests
import socket
str='\u5e02\u573a\u63a5\u53e3\u8bbf\u95ee\u529f\u80fd\u6682\u65f6\u5173\u95ed\uff0c\u8bf7\u7a0d\u540e\u518d\u8bd5'
print(str.encode('utf-8').decode('utf-8'))
a=random.uniform(5, 10)
print(a)
time.sleep(a)
import requests
import utils
import random
import time
import utils
class Get_text(object):
    def __init__(self):
        self.proxies = {'http': '180.120.183.19:38577',
                        'https': '180.120.183.19:38577'
                        }
        cookie=utils.cookie()
        self.cookies = {}
        self.headers = {
            'User-Agent': utils.ua(),
        }
        for line in cookie.split(';'):
            key, value = line.split('=', 1)
            self.cookies[key] = value
    def rst(self,url):
        r = requests.get(url=url, headers=self.headers,proxies=self.proxies)
        time.sleep(random.uniform(5, 10))
        return r.text
