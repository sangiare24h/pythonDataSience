# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductscrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Store = scrapy.Field()
    Name = scrapy.Field()
    Description = scrapy.Field()
    Tags = scrapy.Field()
    Price = scrapy.Field()
    SalePrice = scrapy.Field()
    Image = scrapy.Field()
    Url = scrapy.Field()
