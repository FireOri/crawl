# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.http import Request
from scrapy.pipelines.images import ImagesPipeline


class WallpaperspiderPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for url in item['url']:
            yield Request(url, meta={'name': item['name']})

    def file_path(self, request, response=None, info=None):
        image_guid = request.url.split('/')[-1]
        name = request.meta['name']
        filename = '{0}/{1}'.format(name, image_guid)
        return filename


