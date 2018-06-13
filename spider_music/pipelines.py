# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import spider_music.settings as GLOBAL

class SpiderMusicPipeline(object):
    def process_item(self, item, spider):
        if item['id'] == '':
            item['id'] = item['name']
        print('ddddddddddddeeeeeeeeeeeee')
        return item

class DownloadMusicPipeline(object):
    pass

class StoreMusicPipeline(object):
    pass
