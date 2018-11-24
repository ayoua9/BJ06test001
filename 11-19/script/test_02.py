from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

el1 = driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")
el2 = driver.find_element_by_xpath("//*[contains(@text,'电池')]")
driver.drag_and_drop(el2,el1)
driver.find_element_by_xpath("//*[contains(@text,'安全')]").click()
driver.find_element_by_xpath("//*[contains(@text,'屏幕锁定方式')]").click()
driver.find_element_by_xpath("//*[contains(@text,'图案')]").click()
driver.implicitly_wait(20)

sleep(3)
TouchAction(driver).press(x=238,y=852).wait(100).move_to(x=718-238,y=0).wait(100).\
    move_to(x=1198-718,y=0).wait(100).move_to(x=718-1198,y=1335-852).wait(100).\
    move_to(x=238-718,y=1815-1332).wait(100).release().perform()


sleep(3)
driver.quit()