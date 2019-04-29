import scrapy
from scrapy.http import Request
from WallPaperSpider.items import WallpaperspiderItem


class WallPaperSpider(scrapy.Spider):

    name = 'WallDownload'
    allowed_domains = ['win4000.com']
    base_url = 'http://www.win4000.com'
    start_urls = ['http://www.win4000.com/']

    def parse(self, response):

        urls = response.xpath('//div[@class="area1_lb"]/ul/li/a/@href').extract()
        for url in urls:
            yield Request(self.base_url + url, callback=self.parse_one)

    def parse_one(self, response):

        urls = response.xpath('//ul[@class="clearfix"]/li/a/@href').extract()
        for url in urls:
            if 'wallpaper_detail' in url:
                yield Request(url=url, callback=self.parse_two)

        next_page = response.xpath('//div[@class="pages"]//a[@class="next"]/@href').extract()
        if next_page:
            next_page = next_page[0]
            yield Request(url=next_page, callback=self.parse_one)

    def parse_two(self, response):
        # http://pic1.win4000.com/wallpaper/2018-10-10/5bbd6374c4233.jpg
        item = WallpaperspiderItem()
        original_url = response.xpath('//ul[@id="scroll"]/li/a/img/@data-original').extract()
        url = [url.replace('_120_80', '') for url in original_url]
        name = response.xpath('//div[@class="tit clearfix"]/h2/text()').extract()[1]
        item['url'] = url
        item['name'] = name
        yield item





