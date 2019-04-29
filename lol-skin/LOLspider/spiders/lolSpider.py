# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from ..items import LolspiderItem


class LolspiderSpider(scrapy.Spider):
    name = 'lolSpider'
    allowed_domains = ['qq.com']
    start_urls = ['https://lol.qq.com/data/info-heros.shtml']
    base_url = 'http://lol.qq.com/data/'

    def parse(self, response):
        urls = response.xpath('//ul[@id="jSearchHeroDiv"]/li/a/@href').extract()
        for url in urls:
            yield Request(self.base_url+url, callback=self.parse_one)

    def parse_one(self, response):
        item = LolspiderItem()
        urls = response.xpath('//ul[@id="skinNAV"]/li/a/img/@src').extract()
        urls = ['http:' + url.replace('small', 'big') for url in urls]
        name = response.xpath('//div[@class="defail-data"]/h1/text()').extract_first()
        item['url'] = urls
        item['name'] = name
        yield item






