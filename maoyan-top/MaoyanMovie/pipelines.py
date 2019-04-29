# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from . import settings


class MaoyanmoviePipeline(object):

    def __init__(self):
        # 建立连接
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            port=settings.MYSQL_PORT,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)
        # 获取游标
        self.cur = self.connect.cursor()
        # 创建数据表sql
        self.sql = 'USE maoyan;'
        self.tbsql = '''CREATE TABLE IF NOT EXISTS scrapy(
        id INT(10) PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(100) NOT NULL,
        time VARCHAR(100) NOT NULL,
        image VARCHAR(100) NOT NULL,
        score VARCHAR(100) NOT NULL,
        description VARCHAR(100) NOT NULL,
        actor VARCHAR(100) NOT NULL
        ) AUTO_INCREMENT=1;'''

    def process_item(self, item, spider):
        # 进入数据库
        self.cur.execute(self.sql)
        # 创建数据表
        try:
            self.cur.execute(self.tbsql)
        except BaseException as e:
            print('创建数据表失败,原因是%s' % e)
        # 插入数据
        self.cur.execute('INSERT INTO scrapy(name, time, image, score, description, actor) VALUES ({0}, {1}, {2}, {3}, {4}, {5});'.format(item['name'], item['time'], item['image'], item['score'], item['description'], item['actor']))
        return item
    
    def __del__(self):
        # 断开连接
        self.cur.close()
        # 关闭数据库
        self.connect.close()
