# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from datetime import datetime

class Yes24CrawlSpider(CrawlSpider):
    name = 'yes24_crawl'
    allowed_domains = ['yes24.com']

    start_urls = ['http://www.yes24.com/24/Category/Display/001001046001?ParamSortTp=05',
                  ]

    rules = (
        Rule(LinkExtractor(allow=r'Product/Goods/.*'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'24/Category/Display/001001046001?ParamSortTp=05&PageNumber=\d')),
    )

    def parse_item(self, response):
        item = {}
        item['book_site'] = 'yes24'
        item['book_isbn'] = response.xpath('//*[@id="infoset_specific"]/div[2]/div/table/tbody/tr[3]/td/text()').extract()
        item['book_cat'] = response.xpath('//*[@id="infoset_goodsCate"]/div[2]/dl[1]/dd/ul/li[1]/a[3]/text()').extract()
        item['book_title'] = response.xpath('//*[@id="yDetailTopWrap"]/div[2]/div[1]/div/h2/text()').extract()
        item['book_price'] = response.xpath('//*[@id="yDetailTopWrap"]/div[2]/div[2]/div[1]/div[1]/table/tbody/tr[2]/td/span/em/text()').extract()
        item['book_author'] = response.xpath('//*[@id="yDetailTopWrap"]/div[2]/div[1]/span[2]/span[1]/a/text()').extract()
        item['book_publish'] = response.xpath('//*[@id="yDetailTopWrap"]/div[2]/div[1]/span[2]/span[2]/a/text()').extract()
        item['book_publish_date'] = response.xpath('//*[@id="yDetailTopWrap"]/div[2]/div[1]/span[2]/span[3]/text()').extract()
        item['book_img'] = response.xpath('//*[@id="yDetailTopWrap"]/div[1]/div[1]/span/em/img/@src').extract()
        item['book_url'] = response.request.url
        item["crawl_time"] = datetime.now()
        return item
