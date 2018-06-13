#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-12 16:28:05
# @Author  : lizz (${email})
# @Link    : ${link}
# @Version : $Id$

import os
from spider_music.settings import DEFALUT_DOWNLOAD_TMP_PATH
import uuid
import traceback
import urllib3
import pymysql

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

class SpiderMusicPipeline(object):
    def process_item(self, item, spider):
        if (not ("id" in item)) or (item["id"] is None):
            item["id"] = uuid.uuid1()
        print('ddddddddddddeeeeeeeeeeeeefff')
        return item

class DownloadMusicPipeline(object):

    def process_item(self, item, spider):
        if ("music_url" in item) and (item["music_url"] != ''):
            self.download_file(item["music_url"])
        return item

    @staticmethod
    def download_file(url):
        try:
            http = urllib3.PoolManager(timeout=15)
            response = http.request('GET', url, retries=3)
            file_name_suffix = os.path.basename(url)
            (file_name, file_suffix) = os.path.splitext(file_name_suffix)
            if not os.path.exists(DEFALUT_DOWNLOAD_TMP_PATH):
                os.makedirs(DEFALUT_DOWNLOAD_TMP_PATH)
            local_file_path = os.path.join(DEFALUT_DOWNLOAD_TMP_PATH, file_name_suffix)
            print("local_file_path=", local_file_path)
            with open(local_file_path, 'wb') as f:
                f.write(response.data)
            
            response.release_conn()
            return (f, file_name, file_suffix)
        except Exception as err:
            print(err)
            traceback.print_tb(err.__traceback__)
            response.release_conn()
            return None
    

class StoreMusicPipeline(object):
    def open_spider(self, spider):
        self.db = pymysql.connect("localhost","testuser","test123","TESTDB" )
 
    def process_item(self, item, spider):
        if False:
            return item
        if ("music_url" in item) and (item["music_url"] != ''):
            cursor = self.db.cursor()
            sql = "insert into "
            cursor.execute(sql)
        return item
        

    def close_spider(self, spider):
        self.db.close()

    


 