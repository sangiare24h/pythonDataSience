# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.selector import Selector
from productsCrawler.items import ProductscrawlerItem

class ProductscrawlerSpiderSpider(Spider):
    name = 'productsCrawler_spider'
    allowed_domains = ['www.thegioididong.com','www.tiki.vn']
    start_urls = ['https://www.thegioididong.com/may-doi-tra']

    def parse(self, response):
        questions = Selector(response).xpath("//ul[@class='products']/li")

        for question in questions:
            item = ProductscrawlerItem()

            item['Name'] = question.xpath('a/h3/text()').extract_first()
            item['Price'] = question.xpath('a/div/span[@class="price-line"]/text()').extract_first()
            item['Image'] = question.xpath('a/img/@src').extract_first()

            yield item
