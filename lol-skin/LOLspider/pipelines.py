# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import requests


class LolspiderPipeline(object):

    def process_item(self, item, spider):

        if not os.path.exists('skin'):
            os.mkdir('skin')

        try:
            for url in item['url']:
                res = requests.get(url)
                name = item['name']
                filename = './skin/' + name + '-' + url.split('big')[-1]
                with open(filename, 'wb') as f:
                    f.write(res.content)
        except Exception as e:
            print(e)

