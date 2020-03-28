#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
from selenium import webdriver
import time

def driver():
    desired_caps = {
        "deviceName": "127.0.0.1:21503",
        # "deviceName": "46HDU19118003575",(真机)
        "platformName": "Android",
        "plarformVersion": "5.1.1",
        # "plarformVersion": "10.0",（真机）
        "appPackage": "com.ss.android.article.news",
        "appActivity": "com.ss.android.article.news.activity.MainActivity",
        "noRset": True,
        "unicodeKeyboard": True
        }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
    driver.quit()
    return driver


if __name__ == '__main__':
    driver = driver()
    driver.find_element_by_id('com.ss.android.article.news:id/ag9').click()
    driver.find_element_by_id('com.ss.android.article.news:id/b2c').click()
    driver.find_element_by_id('com.ss.android.article.news:id/bov').click()
    # 选择微头条
    driver.tap([(469, 152)], 2)
    # driver.find_elements_by_ios_uiautomation("new UiSelector().text(\"+发微头条\")")[1].click()
    # 输入微头条内容
    driver.find_element_by_id('com.ss.android.article.news:id/blh').send_keys('test ykykykykyky')
