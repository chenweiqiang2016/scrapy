# -*- coding: utf-8 -*-

# 常用方法 find_element_by_*
# Keys 这个类来模拟键盘输入

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
# print driver.page_source