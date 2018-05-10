#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time


def login_by_cookie(driver,cookie,delay = 1):
    
    try:
        url = 'http://campus.chinaunicom.cn/ilearn/home/unicom/jsp/index.jsp'
        driver.get(url)
        time.sleep(1*delay)
        for i in range(len(cookie)):
            if cookie[i]['name'] == 'SESSIONID':
                continue
            else:
                driver.add_cookie(cookie[i])


        driver.get(url)

    finally:
        pass
    return driver