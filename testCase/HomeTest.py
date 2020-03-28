#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
from common.Driver import driver
import time
from common import MyTest



class HomeTest(MyTest):

    def test_weitoutiao(self):
        # 点击发布
        self.driver.find_element_by_id('com.ss.android.article.news:id/bov').click()
        # 选择微头条
        self.driver.tap([(469, 152)], 2)
        # driver.find_elements_by_ios_uiautomation("new UiSelector().text(\"+发微头条\")")[1].click()
        # 输入微头条内容
        self.driver.find_element_by_id('com.ss.android.article.news:id/blh').send_keys('test ykykykykyky')

        time.sleep(2)

if __name__ == '__main__':
    MyTest.main()