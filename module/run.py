# -*- coding:utf-8 -*-
from util.load_phantomjs import load_phantomjs
import time
from selenium.webdriver.common.keys import Keys

def run(phantomjs,search_url):
    try:
        phantomjs.get(search_url)
        time.sleep(15)
        print(phantomjs.page_source)
        phantomjs.save_screenshot(r'.\bdbutton3.png')
        phantomjs.switch_to.frame(phantomjs.find_element_by_id('topFrame'))
        count = 30
        while count >0:
            print("剩" + str(2*count) + "分钟")
            time.sleep(120)
            a = phantomjs.find_element_by_id('save_span')
            a.click()
            time.sleep(1)
            phantomjs.save_screenshot(r'.\bdbutton4.png') 
            a.send_keys(Keys.ENTER)
            phantomjs.save_screenshot(r'.\bdbutton5.png') 
            count = count - 1
    except:
        print("error2!")
        exit(0)
    return 


