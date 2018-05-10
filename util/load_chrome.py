#!/usr/bin/python3
# -*- coding: utf-8 -*-
from selenium import webdriver


def chrome_less(): 
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    prefs = {
        "profile.content_settings.plugin_whitelist.adobe-flash-player":1,
        "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player":1
    }
    
    chrome_options.add_experimental_option('prefs',prefs)

    driver = webdriver.Chrome(chrome_options=chrome_options)



    return driver



def chrome_test():
    driver = webdriver.Chrome()
    return driver