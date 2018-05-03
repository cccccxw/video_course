# -*- coding:utf-8 -*-
from util.load_phantomjs import load_phantomjs
import time

def login(phantomjs,login_url,search_url= 0):
    
    try:
        phantomjs.get(login_url)
        time.sleep(2)
        user_ID = input("请输入账号")
        user_Pwd = input("密码")
        phantomjs.find_element_by_id('unplay').clear()
        phantomjs.find_element_by_id('unplay').send_keys(user_ID)

        phantomjs.find_element_by_id('pwplay').clear()
        phantomjs.find_element_by_id('pwplay').send_keys(user_Pwd)

        phantomjs.save_screenshot(r'.\bdbutton.png')

        code = input("验证码")

        phantomjs.find_element_by_id('vcode').clear()
        phantomjs.find_element_by_id('vcode').send_keys(code)
        
        phantomjs.find_element_by_class_name('login-btn').click()
        time.sleep(2)
        phantomjs.save_screenshot(r'.\bdbutton.png')
    finally:
        phantomjs.close()
    return 

if __name__ =='__main__':
    phantomjs = load_phantomjs()
    login_url = 'http://campus.chinaunicom.cn/ilearn/en/learner/jsp/login.jsp'
    
    
    print(login(phantomjs,login_url))