from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.1.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.mileclass'
desired_caps['appActivity'] = 'com.mileclass.main.LoadingActivity'

desired_caps['noRest']=True
# desired_caps['appPackage'] = 'com.android.calculator2'
# desired_caps['appActivity'] = 'com.android.calculator2.Calculator'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(30)
# driver.find_element_by_id("com.android.calculator2:id/digit8").click()
# driver.find_element_by_id("com.android.calculator2:id/mul").click()
# driver.find_element_by_id("com.android.calculator2:id/digit8").click()
# driver.find_element_by_id("com.android.calculator2:id/equal").click()
driver.find_element_by_id("com.mileclass:id/edit_account").send_keys("11497")
driver.find_element_by_id("com.mileclass:id/edit_pwd").send_keys("123456a")
driver.find_element_by_id("com.mileclass:id/tv_login").click()



