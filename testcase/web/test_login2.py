import selenium
from  selenium import webdriver
import time
import unittest
import  dbtest
from selenium.webdriver.common.keys import Keys
class demotest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.drver = webdriver.Chrome(r"E:\PYproject\.idea\chromedriver.exe")
        cls.drver.maximize_window()
        cls.drver.implicitly_wait(10)
        cls.url = "http://jackey.mileclass.cn:9949/user/login"
        cls.verificationErrors = []
        cls.accept_next_alert = True
        cls.drver.get(cls.url)
        print(cls.verificationErrors)
    @classmethod
    def tearDownClass(cls):
        cls.drver.quit()
    def login(self,username,password):
        drver = self.drver
        # drver.get('http://jackey.mileclass.cn:9949/user/login')
        # drver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[2]/div[1]/input').clear(username)
        # time.sleep(3)
        drver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/div[1]/div/input').send_keys(username)
        # drver.find_element_by_xpath('//*[@class=\'pwd_item\']').clear(password)
        # time.sleep(3)
        drver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/div[2]/div/input').send_keys(password)
        drver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/button/span').click()


    def test_login_fail(self):
        self.login('11497', '123456')
        drver = self.drver
        # drver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[2]/div[1]/input').send_keys('11497')
        # drver.find_element_by_xpath('//*[@class=\'pwd_item\']').send_keys('123456')
        # drver.find_element_by_xpath('/html/body/div/div[2]/div/div/button').click()
        # time.sleep(3)
        tip = drver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div[3]/div").text
        self.assertEquals(tip, '账户名与密码不匹配，请重新输入')

    def test_login_success(self):
        drver = self.drver
        time.sleep(3)
        # drver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[2]/div[1]/input').clear()
        # drver.find_element_by_xpath('//*[@class=\'pwd_item\']').clear()
        ele1 = drver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/div[1]/div/input')
        ele2 = drver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/div[2]/div/input')
        ele1.send_keys(Keys.CONTROL+'a')
        ele1.send_keys(Keys.DELETE)
        ele2.send_keys(Keys.CONTROL+'a')
        ele2.send_keys(Keys.DELETE)
        self.login('11497','123456a')
        time.sleep(5)
        getsql = dbtest.sqlclass.excutesql(sql="SELECT * FROM uc_user_register WHERE username = '11497';")
        tip = drver.find_element_by_xpath('/html/body/div/div[1]/div/div/span[4]/span[1]').text
        self.assertIn(tip, '梁晓蝶')
        drver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/ul/li[2]/a/span').click()
        time.sleep(3)



if __name__ == '__main__':
    unittest.main()
