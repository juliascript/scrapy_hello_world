# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["http://quotes.toscrape.com/"]
    start_urls = ['http://quotes.toscrape.com//']

    def parse(self, response):
        quotes = response.xpath('//*[@class="quote"]')

        for quote in quotes:
        	text = quote.xpath('.//*[@class="text"]/text()').extract_first()
        	# print text
        	author = quote.xpath('.//*[@class="author"]/text()').extract_first()
        	# print author

        	# tags = quote.xpath('.//*[@itemprop="keywords"]/@content').extract_first().split(',')
        	tags = quote.xpath('.//*[@class="tag"]/text()').extract()
        	tag_links = quote.xpath('.//*[@class="tag"]/@href').extract()
        	# print tag_links
        	# print tags

        	yield {
        		'text': text,
        		'author': author,
        		'tags': {
        			'tag_names': tags,
        			'tag_links': tag_links
        		}
        	}
