from crawer import Buff
def run():
    f=open('data/cookie.txt','r')
    cookie=f.read()
    f.close()
    b=Buff(cookie,42000)
    b.write()
run()