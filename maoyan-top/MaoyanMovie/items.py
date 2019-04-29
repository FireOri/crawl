# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanmovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()   # 电影名
    time = scrapy.Field()   # 上映时间
    image = scrapy.Field()  # 海报封面
    score = scrapy.Field()  # 评分
    description = scrapy.Field()  # 简介
    actor = scrapy.Field()  # 演员表
