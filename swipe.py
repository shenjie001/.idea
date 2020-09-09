from  appium import webdriver


class Swipe():
    desired_caps = desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '9'
    desired_caps['deviceName'] = 'ce1f2e31'
    desired_caps['appPackage'] = 'com.mileclass'
    desired_caps['appActivity'] = 'com.mileclass.main.LoadingActivity'
    desired_caps['noRest'] = True

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)



    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)


    def swipeLeft(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.75)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.25)
        self.driver.swipe(x1, y1, x2, y1, t)


    def swipeRight(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.25)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.75)
        self.driver.swipe(x1, y1, x2, y1, t)


    def swipeUp(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.75)  # 起始y坐标
        y2 = int(l[1] * 0.25)  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2, t)


    def swipeDown(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.25)  # 起始y坐标
        y2 = int(l[1] * 0.75)  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2, t)
