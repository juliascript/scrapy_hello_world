# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from quotes_spider.items import QuotesSpiderItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ['http://quotes.toscrape.com//']

    def parse(self, response):
        quotes = response.xpath('//*[@class="quote"]')

        for quote in quotes:

        	l = ItemLoader(item=QuotesSpiderItem(), response=response)
        	text = quote.xpath('.//*[@class="text"]/text()').extract_first()
        	# print text
        	author = quote.xpath('.//*[@class="author"]/text()').extract_first()
        	# print author

        	# tags = quote.xpath('.//*[@itemprop="keywords"]/@content').extract_first().split(',')
        	tags = quote.xpath('.//*[@class="tag"]/text()').extract()
        	tag_links = quote.xpath('.//*[@class="tag"]/@href').extract()
        	# print tag_links
        	# print tags

        	# yield {
        	# 	'text': text,
        	# 	'author': author,
        	# 	'tags': {
        	# 		'tag_names': tags,
        	# 		'tag_links': tag_links
        	# 	}
        	# }

        	l.add_value('text', text)
        	l.add_value('author', author)
        	l.add_value('tags', {
        			'tag_names': tags,
        			'tag_links': tag_links
        		})

        	yield l.load_item()

        next_pg_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        abs_next_pg_url = response.urljoin(next_pg_url)
        print abs_next_pg_url

        # yield scrapy.http.Request(abs_next_pg_url, callback=self.parse)
        yield scrapy.http.Request(abs_next_pg_url)


