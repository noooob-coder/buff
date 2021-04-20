import json
from get_txt import Get_text
class Get_id(object):
    def __init__(self):
        self.url='https://buff.163.com/api/market/goods?game=csgo&page_num=1&category='
        self.weapon_list=self.read('./data/goods.txt')
        self.id_path='./data/id.txt'
        self.get_text=Get_text()
    def read(self,path):
        weapon_list=[]
        f=open(path,'r',encoding='utf-8')
        for line in f.readlines():
            line=line.replace(' ','')
            line=line.replace('-','')
            line=line.replace('\n','')
            weapon_list.append(line)
        f.close()
        self.weapon_list=weapon_list
        return weapon_list
    def id(self):
        data={}
        data['name']=[]
        data['buy_max_price'] = []
        data['buy_num']= []
        data['quick_price']=[]
        data['id']=[]
        data['sell_min_price']=[]
        data['sell_num']=[]
        data['sell_reference_price']=[]
        f = open('data/base_data.txt', 'a', encoding='utf-8')
        all_lis=[]
        for item in self.weapon_list:
            page_num=self.get_page(item)
            for i in range(page_num):
                url='https://buff.163.com/api/market/goods?game=csgo&page_num='+str(i)+'&category='+item
                text=self.get_text.rst(url)
                dic=json.loads(text)
                test=open('test.html','w',encoding='utf-8')
                test.write(text)
                test.close()
                if dic['code']=='OK':
                    item_list=dic['data']['items']
                    for good_item in item_list:
                        data['name'].append(good_item['name'])
                        data['buy_max_price'].append(good_item['buy_max_price'])
                        data['buy_num'].append(good_item['buy_num'])
                        data['id'].append(good_item['id'])
                        data['quick_price'].append(good_item['quick_price'])
                        data['sell_min_price'].append(good_item['sell_min_price'])
                        data['sell_num'].append(good_item['sell_num'])
                        data['sell_reference_price'].append(good_item['sell_reference_price'])
                        str=data['name']+'\t'+data['buy_max_price']+'\t'+['buy_num']+'\t'+data['id']+'\t'+data['quick_price']+'\t'+data['sell_min_price']+'\t'+data['sell_num']+'\t'+data['sell_reference_price']
                        f.write(str+'\n')
                print("完成"+item)
        f.close()
        self.to_text(data['name'], './data/name.txt')
        self.to_text(data['buy_max_price'],'./data/buy_max_price.txt')
        self.to_text(data['buy_num'],'./data/buy_num.txt')
        self.to_text(data['id'],'./data/id.txt')
        self.to_text(data['quick_price'],'./data/quick_price.txt')
        self.to_text(data['sell_min_price'],'./data/sell_min_price.txt')
        self.to_text(data['sell_num'],'./data/sell_num.txt')
        self.to_text(data['sell_reference_price'],'./data/sell_reference_price.txt')
        # df=pd.DataFrame(data)
        # df.to_excel('/data/goods_data.xlsx')
    def to_text(self,data,path):
        f=open(path,'w',encoding='utf-8')
        for i in data:
            f.write(i)
        f.close()
    def get_page(self,weapon):
        url=self.url+weapon
        text=self.get_text.rst(url)
        test = open('test.html', 'w', encoding='utf-8')
        test.write(text)
        test.close()
        dic = json.loads(text)
        return int(dic['data']['total_page'])

c=Get_id()
c.id()