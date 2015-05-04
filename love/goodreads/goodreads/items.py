# -*- coding: utf-8 -*-
import scrapy


class GrItem(scrapy.Item):
	quotes = scrapy.Field()
	link = scrapy.Field()
