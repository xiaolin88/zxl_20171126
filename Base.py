# coding: utf-8
from appium import webdriver
import unittest
import time

class demo(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'fceac6e79804'
        desired_caps['appPackage'] = 'com.sina.weibo'
        desired_caps['appActivity'] = 'com.sina.weibo.SplashActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def test_add01(self):
        time.sleep(5)
        self.driver.find_element_by_id('titleSave').click()
        self.driver.find_element_by_id('etLoginUsername').clear()
        time.sleep(3)
        self.driver.find_element_by_id('etLoginUsername').send_keys('liangmu006@163.com')
        time.sleep(3)
        self.driver.find_element_by_id('etPwd').send_keys('lm15164565107')
        self.driver.find_element_by_id('rlLogin').click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@Text='我的相册']")


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
        unittest.main()

