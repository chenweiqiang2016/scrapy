# -*- coding:utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()


	def test_search_in_python_org(self):
		driver = self.driver
		driver.get("http://www.python.org")
		self.assertIn("Python", driver.title)
		elem = driver.find_element_by_name("q")
		#你可以对任何获取到到元素使用 send_keys 方法
		elem.send_keys("pycon") 
		elem.send_keys(Keys.RETURN)
		assert "No results found." not in driver.page_source

	def tearDown(self): #析构方法
		self.driver.close()

if __name__ == "__main__":
	unittest.main()