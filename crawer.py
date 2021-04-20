import requests
from lxml import etree
import json
import pandas as pd
import datetime
import csv
import time
import matplotlib.pyplot as plt
import utils
from matplotlib.font_manager import FontProperties
import numpy as np
from get_txt import Get_text
class Buff(object):
    def __init__(self,no):
        self.url1 = 'https://buff.163.com/api/market/goods/price_history/buff?game=csgo&goods_id=' + str(no)
        self.url2 = 'https://buff.163.com/market/goods?goods_id=' + str(no) + '&from=market#tab=selling'
        self.get_text=Get_text()
    def getChineseFont(self):
        return FontProperties(fname='C:/Windows/Fonts/simsun.ttc')
    def get_inner_html(self,node):
        html = etree.tostring(node, encoding="utf8").decode('utf8')
        p_begin = html.find('>') + 1
        p_end = html.rfind('<')
        return html[p_begin: p_end]
    def remove_duplicate(self,one_list):
        result_list=[]
        temp_list=sorted(one_list)
        i=0
        while i<len(temp_list):
            if temp_list[i] not in result_list:
                result_list.append(temp_list[i])
            else:
                i+=1
        return result_list
    def view(self):
        flag=0
        try:
            ro=self.get_text.rst(self.url2)
            tree = etree.HTML(ro)
            f=open('test.html','w',encoding='utf-8')
            f.write(ro)
            self.name = self.get_inner_html(tree.xpath("//*[@class='cru-goods']")[0])
        except:
            flag=1
        return flag
    def write(self):
        flag=self.view()
        if flag==0:
            rresult = json.loads(self.get_text.rst(self.url1))
            price_history = rresult['data']['price_history']
            price_index = []
            price_values = []
            for j, i in enumerate(price_history):
                get_time = datetime.datetime.fromtimestamp(i[0] / 1000)
                strtime = get_time.strftime('%Y-%m-%d %H:%M:%S')
                price_history[j][0] = strtime
                price_index.append(get_time)
                price_values.append(i[1])
            name = self.name.replace('|', '')
            name = name.replace('*', '')
            name = name.replace(':', '')
            name = name.replace('"', '')
            name = name.replace(' ', '')
            fileopen = 0
            path='result/'+name + '.csv'
            try:
                open(path)
            except:
                fileopen = 1
            if fileopen==1:
                with open(path, 'w', encoding='utf-8', newline='') as f:
                    csv_writer = csv.writer(f)
                    for i in range(len(price_index)):
                        csv_writer.writerow([price_index[i], price_values[i]])
            else:
                with open(path, 'r') as f:
                    f_csv = csv.reader(f)
                    price_list = []
                    for row in f_csv:
                        for i in row:
                            row[1] = float(row[1])
                        price_list.append(row)
                price_list.extend(price_history)
                price_list = self.remove_duplicate(price_list)  ## 重复数据删除数据更新
                with open(path, 'w', encoding='utf-8', newline='') as f:
                    csv_writer = csv.writer(f)
                    for i in range(len(price_list)):
                        csv_writer.writerow([price_list[i][0], price_list[i][1]])
        else:print("获取失败")





