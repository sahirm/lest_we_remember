# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
#

import scrapy


class LwrItem(scrapy.Item):

    Month = scrapy.Field()
    Year = scrapy.Field()

    Date = scrapy.Field()
    Type = scrapy.Field()
    Dead = scrapy.Field()
    Injured = scrapy.Field()
    Location = scrapy.Field()
    Details = scrapy.Field()
    Perpetrator = scrapy.Field()
    State = scrapy.Field()
    Nonstate = scrapy.Field()
    Partof = scrapy.Field()


