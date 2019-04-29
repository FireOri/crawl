# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from ..items import MaoyanmovieItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/board']
    base_url = 'https://maoyan.com'

    def parse(self, response):
        urls = response.xpath('//dl[@class="board-wrapper"]/dd/a/@href').extract()
        for url in urls:
            yield Request(self.base_url + url, callback=self.parse_one)

    def parse_one(self, response):
        item = MaoyanmovieItem()
        image = response.xpath('//div[@class="avatar-shadow"]/img/@src').extract_first()
        name = response.xpath('//div[@class="movie-brief-container"]/h3/text()').extract_first()
        time = response.xpath('//div[@class="movie-brief-container"]/ul/li[3]/text()').extract_first()[:10]
        score = response.xpath('//span[@class="stonefont"]/text()').extract_first()
        description = response.xpath('//span[@class="dra"]/text()').extract_first()
        actors = response.xpath('//li[@class="celebrity actor"]/div/a/text()').extract()
        actor = str([actor.replace('\n', '').strip('      ') for actor in actors])
        item['name'] = name
        item['time'] = time
        item['image'] = image
        item['score'] = score
        item['description'] = description
        item['actor'] = actor
        yield item




