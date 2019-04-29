# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
from scrapy import signals
from selenium import webdriver
from scrapy.http import HtmlResponse


class SeleniumMiddleware(object):

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.implicitly_wait(10)

    def __del__(self):
        self.driver.quit()

    def process_request(self, request, spider):
        driver = self.driver
        try:
            driver.get(request.url)
            html = driver.execute_script("return document.documentElement.outerHTML")
            return HtmlResponse(request.url, body=html, encoding='utf-8', request=request)
        except Exception as e:
            print(e)

