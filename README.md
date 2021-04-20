#网易buff csgo饰品的半成品爬虫
##使用说明
###先利用浏览器获取自己账号的cookie存放在data/cookie.txt文件中
###默认采用ip代理模式，将自己申请到的获取代理IP的api填写到utils.py相应位置
###get_id.py用于每个饰品的id、name、buy_max_price、buy_num、quick_price、sell_min_price、sell_num、sell_reference_price等信息，并存放在相应目录下
###crawer.py用于获取指定饰品过去7天的价格
