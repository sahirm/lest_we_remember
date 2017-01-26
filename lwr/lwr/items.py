# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
#

import scrapy


class LwrItem(scrapy.Item):
    # define the fields for your item here like:
    month = scrapy.Field()
    year = scrapy.Field()
    url = scrapy.Field()
    day = scrapy.Field()
    type = scrapy.Field()
    dead = scrapy.Field()
    injured = scrapy.Field()
    location = scrapy.Field()
    details = scrapy.Field()
    perpetrator = scrapy.Field()
    source = scrapy.Field()

