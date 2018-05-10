#!/usr/bin/python3
# -*- coding: utf-8 -*-

import threading
import time

from PIL import Image
from selenium.webdriver.common.keys import Keys



def login(driver,user_name,user_pwd,delay = 1):
    
    try:
        login_url = 'http://campus.chinaunicom.cn/ilearn/en/learner/jsp/login.jsp'
        driver.get(login_url)
        time.sleep(2*delay)
        driver.save_screenshot(r'./code.png')
        
        code_element = driver.find_element_by_id("code")

        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.location['x'] + code_element.size['width']
        bottom = code_element.location['y'] + code_element.size['height']

        im = Image.open(r'./code.png')
        im = im.crop((left, top, right, bottom))
        im.save(r'./code.png')
        class ThreadClass(threading.Thread):
            def run(self):
                code_im=Image.open(r'./code.png')
                code_im.show()
                time.sleep(1.5)
            def stop(self):
                self.stopped = True
        code_show = ThreadClass()
        code_show.start()



        user_ID = user_name
        user_Pwd = user_pwd

        driver.find_element_by_id('unplay').clear()
        driver.find_element_by_id('unplay').send_keys(user_ID)

        driver.find_element_by_id('pwplay').clear()
        driver.find_element_by_id('pwplay').send_keys(user_Pwd)


        code = input("验证码")

        driver.find_element_by_id('vcode').clear()
        driver.find_element_by_id('vcode').send_keys(code)
        
        driver.find_element_by_class_name('login-btn').click()
        time.sleep(2*delay)

    except Exception as e:
        print(e)
        print('error in login')
        return 0
    return driver
