# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



def load_phantomjs():
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.103 Safari/537.36" )

    
    phantomjs = webdriver.PhantomJS(executable_path=r'.\phantomjs.exe',desired_capabilities=dcap)
    #phantomjs.set_window_size(20,20)
    return phantomjs
