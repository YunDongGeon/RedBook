# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from datetime import datetime

class InterparkCrawlSpider(CrawlSpider):
    name = 'interpark_crawl'
    allowed_domains = ['book.interpark.com']
    start_urls = [
                    'http://book.interpark.com/display/displaylist.do?_method=module&sc.dispNo=028005001&sc.shopNo=0000400000&query=&view_type=detail&pageSz=20&sort=bestseller&sale_st=Y&pageSn=1&view_filter=all_book&bookblockname=',
                    'http://book.interpark.com/display/displaylist.do?_method=module&sc.dispNo=028005001&sc.shopNo=0000400000&query=&view_type=detail&pageSz=20&sort=bestseller&sale_st=Y&pageSn=21&view_filter=all_book&bookblockname=',
                    'http://book.interpark.com/display/displaylist.do?_method=module&sc.dispNo=028005001&sc.shopNo=0000400000&query=&view_type=detail&pageSz=20&sort=bestseller&sale_st=Y&pageSn=41&view_filter=all_book&bookblockname=',
                    'http://book.interpark.com/display/displaylist.do?_method=module&sc.dispNo=028005001&sc.shopNo=0000400000&query=&view_type=detail&pageSz=20&sort=bestseller&sale_st=Y&pageSn=61&view_filter=all_book&bookblockname=',
                    'http://book.interpark.com/display/displaylist.do?_method=module&sc.dispNo=028005001&sc.shopNo=0000400000&query=&view_type=detail&pageSz=20&sort=bestseller&sale_st=Y&pageSn=81&view_filter=all_book&bookblockname=',
                ]

    rules = (
        Rule(LinkExtractor(allow=r'product/BookDisplay.do\?_method=Detail&sc.shopNo=.*.&dispNo=&sc.prdNo=.*.&sc.saNo=.*'),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        # 쇼핑몰 이름
        item["book_site"] = "인터파크도서"
        # 책 제목
        item["book_title"] = response.xpath('//*[@id="inc_titWrap"]/div[1]/div/p/text()')[0].extract().strip()
        # 책 카테고리
        item["book_cat"] = response.xpath('//*[@id="locationMenu3"]/text()')[0].extract()
        # 책 가격
        item["book_price"] = response.xpath('//*[@id="inc_optionWrap"]/div[2]/div[4]/div[1]/ul/li[1]/div/p[1]/span[1]/text()')[0].extract()
        # 책 작가
        item["book_author"] = response.xpath('//*[@id="inc_optionWrap"]/div[2]/div[2]/ul/li[1]/a/text()')[0].extract()
        # 책 출판사
        item["book_publish"] = response.xpath('//*[@id="hdelvMafcEntrNm"]/text()')[0].extract()
        # 책 출판일
        item["book_publish_date"] = response.xpath('//*[@id="inc_optionWrap"]/div[2]/div[2]/ul/li[3]/text()')[0].extract()
        # 책 이미지
        item["book_img"] = response.xpath('//*[@id="inc_optionWrap"]/div[1]/div[1]/div/div/div/img/@src')[0].extract()
        # 책 쇼핑몰 상세보기 주소
        item["book_url"] = response.request.url
        # 크롤링된 시간
        item["crawl_time"] = datetime.now()
        return item
