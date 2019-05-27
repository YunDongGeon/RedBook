# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from datetime import datetime


class AuctionCrawlSpider(CrawlSpider):
    name = 'aladin_crawl'
    allow_domains = ['aladin.co.kr']

    start_urls = [
        'https://www.aladin.co.kr/shop/wbrowse.aspx?BrowseTarget=List&ViewRowsCount=25&ViewType=Detail&PublishMonth=0&SortOrder=2&page=1&Stockstatus=1&PublishDay=84&CID=50917',
        'https://www.aladin.co.kr/shop/wbrowse.aspx?BrowseTarget=List&ViewRowsCount=25&ViewType=Detail&PublishMonth=0&SortOrder=2&page=2&Stockstatus=1&PublishDay=84&CID=50917&CustReviewRankStart=&CustReviewRankEnd=&CustReviewCountStart=&CustReviewCountEnd=&PriceFilterMin=&PriceFilterMax='
    ]

    rules = (
        Rule(LinkExtractor(allow=r'wproduct.aspx\?ItemId=.*'),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        item['book_site'] = '알라딘'
        try:
            item['book_isbn'] = response.xpath('//*[@id="Ere_prod_allwrap"]/div[11]/div[1]/div[3]/div[1]/ul/li[5]/text()')[0].extract()
        except IndexError:
            return 1
        item['book_cat'] = response.xpath('//*[@id="ulCategory"]/li[1]/a[3]/text()')[0].extract()
        item['book_title'] = response.xpath('//*[@id="Ere_prod_allwrap"]/div[3]/div[2]/div[1]/div/ul/li[1]/div/a[1]/text()')[0].extract()
        item['book_price'] = response.xpath('//*[@id="Ere_prod_allwrap"]/div[4]/div[4]/div/div[3]/ul/li[2]/div[2]/span/text()')[0].extract()
        #info = response.xpath('//*[@id="Ere_prod_allwrap"]/div[3]/div[2]/div[1]/div/ul/li[2]/text()')[0].extract()
        item['book_author'] = response.xpath('//*[@id="Ere_prod_allwrap"]/div[3]/div[2]/div[1]/div/ul/li[2]/a/text()')[0].extract()
        #item['book_publish'] = response.xpath('//*[@id="ucBookItemInfo_htrPublisher"]/p[2]/text()')[0].extract()
        #item['book_publish_date'] = response.xpath('//*[@id="frmMain"]/ul/li[5]/div/div/ul/li[4]/p[2]/text()')[0].extract()
        #item['book_img'] = response.xpath('///*[@id="content"]/div[2]/div[1]/div/div/ul/li[1]/a/img/@src')[0].extract()
        #item['book_url'] = response.request.url
        #item["crawl_time"] = datetime.now()
        return item
