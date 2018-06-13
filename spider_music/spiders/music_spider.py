#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-12 10:23:08
# @Author  : lizz (${email})
# @Link    : ${link}
# @Version : $Id$

import os
import scrapy
from spider_music.items import SpiderMusicItem

class MusicSpider(scrapy.Spider):
    name = "music_spider"
    start_urls = [
        "http://www.9ku.com/music/t_m_hits.htm"
    ]

    def parse(self, response):
        current_url = response.url
        
        context_path = current_url[0:current_url.index("/", 7)]
        count = 0
        for li in response.xpath("//ol/li"):
            count+=1
            if count > 2:
                break
            item = SpiderMusicItem()
            item['name'] = li.xpath("a/text()").extract()[0]
            item['url'] = self.get_path(li.xpath("a/@href").extract()[0], current_url, context_path)
            item['remark'] = item['name'] + r'fj9)'
            yield item
            if item['url'] != '':
                print("ccccccccccccccccccccccccccccccccccccccccccccccccccccc")
                print(item['url'])
                yield scrapy.Request(item['url'], callback=self.parse_download, meta=item)

    def parse_download(self, response):
        print("a333333333333333333333333333")
        item = response.request.meta
        

        #item['music_url'] = response.xpath("//div[@id=kuPlayer]/audio/@src").extract()[0]
        item['music_url'] = "http://mp3.9ku.com/m4a/663208.m4a"
        return item
        
        
    
    @staticmethod
    def get_path(url, current_url, context_path):
        tmp = ""
        if url.startswith("/"):
            tmp = context_path + url
        else:
            tmp = current_url + "/" + url

        return tmp



