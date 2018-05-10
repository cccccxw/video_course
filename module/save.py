#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time

from selenium.webdriver.common.keys import Keys

from util.load_chrome import chrome_less, chrome_test


def save(driver,delay = 1):
    try:
        time.sleep(2*delay)
        driver.save_screenshot(r'./ing.png')
        a = driver.find_element_by_id('save_span')
        a.click()
        time.sleep(2*delay)

        a.send_keys(Keys.ENTER) 

    finally:
        pass
    return 
