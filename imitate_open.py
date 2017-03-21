# -*- coding: utf-8 -*-

# 报错情形
# 1. 没有装 Chrome 浏览器
# 2. Chrome 驱动没有配置在环境变量里

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')