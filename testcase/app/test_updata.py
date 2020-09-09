from  appium import webdriver
import time
import unittest
import  dbtest
import swipe
from swipe import Swipe
from selenium.webdriver.common.keys import Keys
class democlass(unittest.TestCase):

    # def __init__(self,driver):
    #     self.driver = driver
    #     unittest.TestCase.__init__(self)
    rolls = Swipe()
    @classmethod
    def setUpClass(cls):
        desired_caps = desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9.0.2'
        desired_caps['deviceName'] = 'ce1f2e31'
        desired_caps['appPackage'] = 'com.mileclass'
        desired_caps['appActivity'] = 'com.mileclass.main.LoadingActivity'
        desired_caps['noRest'] = True
        desired_caps['appWaitactivity']= 'com.mileclass.main.LoadingActivity'
        desired_caps['sessionOveride'] =True
        #
        # cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        cls.driver.implicitly_wait(60)
    def test_01(self):
       # dbtest.sqlclass.excutesql("UPDATE mile_release_version SET  force_update ='f' , is_gray = 'f' ,version_code = '31' WHERE id = '19'")
        #登录
        self.driver.find_element_by_id("com.mileclass:id/tv_agree").click()
        self.driver.find_element_by_id("com.mileclass:id/edit_account").send_keys("11497")
        self.driver.find_element_by_id("com.mileclass:id/edit_pwd").send_keys("123456a")
        self.driver.find_element_by_id("com.mileclass:id/tv_login").click()



    # def test_normalupdate(self):
    #     self.driver.find_element_by_id("com.mileclass:id/tab_choose_center_txt").click()
    #     tip= self.driver.find_element_by_id("com.mileclass:id/tv_title").text
    #     self.assertIn(tip,"版本升级")

    def test_02(self):
        #登出
        self.driver.find_element_by_id("com.mileclass:id/tab_my").click()
        self.driver.find_element_by_id("com.mileclass:id/liner_setting").click()
        self.rolls.swipeDown(t=1000)
        self.driver.find_element_by_id("com.mileclass:id/tv_login_out").click()
        self.driver.find_element_by_id("com.mileclass:id/tv_confirm").click()

if __name__ == '__main__':
    unittest.main()
