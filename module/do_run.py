#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time

from module.login import login
from module.login_by_cookie import login_by_cookie
from module.save import save
from module.get_course import get_course
from module.get_url import get_url
from util.load_chrome import chrome_less, chrome_test
from util.load_phantomjs import load_phantomjs
from util.set_cookie_str import set_cookie_str

def do_run(title_url,user_name,user_pwd,delay = 1.0):
    try:
        driver = chrome_less()
        driver = login(driver,user_name,user_pwd,delay)
        time.sleep(2*delay)
        cookie = driver.get_cookies()
        cookie_str = set_cookie_str(cookie)
        #调用get_url获取课程列表，筛除已完成课程
        url_list = get_url(driver,cookie,title_url,delay)[0]
        time_list_coe = get_url(driver,cookie,title_url,delay)[1]
        print("找到了"+str(len(url_list))+"个")
        count = int(input("要开几个："))
        time_space =  60 - 4*(count*delay)
        video_url_list = url_list[:count]
        time_list_coe_count = time_list_coe[:count]
        #调用get_course进行获取课程
        video_url = []
        time_list = []
        for i in range(len(video_url_list)):
            video_url.append(get_course(video_url_list[i],cookie_str)[0])
            time_list.append(int(time_list_coe_count[i] * get_course(video_url_list[i],cookie_str)[1])+1)
            if count > 15:
                time_list[i] = (15/count)*time_list[i]
        time_i = max(time_list)
        print(time_i)
    except Exception as e:
        if driver:
            print(e)
            exit(0)
        else:
            return 1 #回去重新登录
    finally:
        try:
            driver.quit()
        except:
            pass

    try:
        driver_video = []
        for i in range(len(video_url)):
            if video_url[i]:
                driver_video.append(load_phantomjs())
                driver_video[i] = login_by_cookie(driver_video[i],cookie,delay)
                time.sleep(3*delay)
                driver_video[i].get(video_url[i])
                time.sleep(3*delay)
                driver_video[i].save_screenshot(r'./star.png')
                print("打开第"+str(i+1)+("个"))
        print("开了"+str(len(driver_video))+"个")
    finally:
        pass
    try:
        for i in range(len(driver_video)):
            driver_video[i].switch_to.frame(driver_video[i].find_element_by_id('topFrame'))
            time.sleep(0.5)
        while time_i >0:
            print("还剩"+str(time_i)+"分钟")
            for i in range(len(driver_video)):
                save(driver_video[i],delay)
            if time_space > 0:
                time.sleep(time_space)
            time_i = time_i - 1
            time_list[i] = time_list[i] -1
            if time_list[i] < 0:  #看完就关掉
                driver_video[i].quit()
                driver_video.pop(i)
                time_list.pop(i)
                i = i - 1
                if len(driver_video)<15:
                    time_space = time_space + 4*delay
                print("看完了一个")

    finally:
        for i in range(len(driver_video)):
            driver_video[i].quit()
    return 0