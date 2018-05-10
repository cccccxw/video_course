#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re

import requests
from bs4 import BeautifulSoup


def get_course(url,cookie_str):
    try:
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'
        headers['Cookie'] = cookie_str
        #print(cookie_str)
        url_text = requests.get(url,headers = headers).text
        #print(url_text)
        bs_obj = BeautifulSoup(url_text,"lxml")
        ele = bs_obj.findAll('a',{'class':'select'})
        #print(ele)
        url_got = str(ele[0].attrs['href'])  #video链接
        
        time_ele_a = bs_obj.findAll('table')
        time_ele_b = time_ele_a[0].findAll('span')
        time_ele_c = time_ele_b[1]
        #print(ele)
        #url_got = str(ele[0].attrs['href'])
        time_ele_d = re.findall(r"\d+\.?\d*",str(time_ele_c))
        time_ele = 50*float(time_ele_d[0])   #video课时
        return url_got,time_ele
    except:
        print("get course error!")
