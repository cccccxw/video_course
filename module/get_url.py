#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import time

import requests
from bs4 import BeautifulSoup

from util.set_cookie_str import set_cookie_str


def get_url(driver,cookie_list,url,delay = 1):
    try:
        driver.get(url)
        time_left_i = []   #过渡list
        url_list = []   #过渡list
        time_left = []
        url_list_got = [] 
        url_ele = []
        time.sleep(5*delay)
        for i in range(5):
            url_ele = driver.find_elements_by_class_name("media-body")  
        
            url_ele = list(set(url_ele))
            url_ele_find = url_ele[:]

            for i in range(len(url_ele)):
                try:
                    span_ele = url_ele[i].find_elements_by_tag_name('span')
                except:
                    print("except one")
                    continue
                if span_ele[1].text == '100%':
                    continue
                else:
                    try:
                        time_left_i.append(1 - float(span_ele[1].text.strip('%'))/100.0)
                        video_ele = url_ele_find[i].find_element_by_class_name('ib-danger')
                        url_list.append(video_ele.get_attribute('href'))
                    except:
                        print('pass one')

            try:
                next_page_ele = driver.find_elements_by_class_name("laypage_next")
                for i in range(len(next_page_ele)):
                    next_page_ele[i].click()
                time.sleep(0.5*delay)
            except:
                break
                print("get url click error!")
        for i in range(len(url_list)):
            if url_list[i] not in url_list_got:
                url_list_got.append(url_list[i])
                time_left.append(time_left_i[i])
    finally:
        pass
    return url_list_got,time_left
