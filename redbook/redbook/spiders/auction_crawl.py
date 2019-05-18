# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AuctionCrawlSpider(CrawlSpider):
    name = 'auction_crawl'
    allow_domains = ['auction.co.kr']

    start_urls = [
    'http://browse.auction.co.kr/list?category=36060105&s=8&t=a'
    ]

    rules = (
        Rule(LinkExtractor(allow=r'http://itempage3.auction.co.kr/DetailView.aspx\?itemno=.*'),
             callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'http://browse.auction.co.kr/list\?category=.*.+&s=8+&t=a+&k=0+&p=\d'),
             callback='parse_url', follow=True)
    )


    def parse_url(self, response):
        url = {}
        return url

    def parse_item(self, response):
        i = {}
        i['book_site'] = '옥션'
        i['book_title'] = response.xpath('//*[@id="frmMain"]/h1/span/text()').extract()
        i['book_cat'] = response.xpath('//*[@id="locbar"]/div/div[1]/div[4]/a/strong/text()').extract()
        i['book_price'] = response.xpath('//*[@class="price_real"]/text()').extract()
        i['book_author'] = response.xpath('//*[@id="ucBookItemInfo_htrAuthor"]/p[2]/text()').extract()
        i['book_publish'] = response.xpath('//*[@id="ucBookItemInfo_htrPublisher"]/p[2]/text()').extract()
        i['book_publish_date'] = response.xpath('//*[@id="frmMain"]/ul/li[5]/div/div/ul/li[4]/p[2]/text()').extract()
        i['book_img'] = response.xpath('///*[@id="content"]/div[2]/div[1]/div/div/ul/li[1]/a/img/@src').extract()
        i['book_url'] = response.request.url #완료
        return i
