#coding:utf-8

"""
1.继承unittest父类，方便testcase使用
2.初始化和清理方法
"""
import unittest,time
from common.Driver import driver
import logging


class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('执行初始化类方法')
        d = driver()
        cls.driver = d.startUp()


    def setUp(self):
        print('执行初始化方法')
        self.driver.launch_app()
        time.sleep(4)

    def tearDown(self):
        print('执行清理方法')
        self.driver.close_app()

    @classmethod
    def tearDownClass(cls):
        print('执行清理类方法')
        cls.driver.quit()


#
if __name__ == '__main__':
    unittest.main()
