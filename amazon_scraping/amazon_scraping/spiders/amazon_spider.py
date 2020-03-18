# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonScrapingItem

class AmazonSpiderSpider(scrapy.Spider):
	name = 'amazon'
	start_urls = [
		'https://www.amazon.in/s?k=last+months+top+selling+books&ref=nb_sb_noss'
	]

	def parse(self, response):
		items = AmazonScrapingItem()

		product_name = response.css('.a-color-base.a-text-normal ::text').extract()
		product_author = response.css('.a-color-secondary .a-size-base+ .a-size-base').css('::text').extract()
		product_price = response.css('.index\=16 .a-spacing-mini .a-color-base .a-row , .a-color-price , .rush-component .rush-component .a-price-whole').css('::text').extract()
		product_imagelink = response.css('.s-image::attr(src)').extract()

		items['product_name'] = product_name
		items['product_author'] = product_author
		items['product_price'] = product_price
		items['product_imagelink'] = product_imagelink

		yield items
		