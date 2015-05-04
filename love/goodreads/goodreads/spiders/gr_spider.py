import scrapy
from goodreads.items import GrItem
 
class GrSpider(scrapy.Spider):
	name = "gr"
	allowed_domains = ["goodreads.com"]
	start_urls = [
		"https://www.goodreads.com/quotes/tag/love"
	]

	def parse(self, response):
		item = GrItem() 
		#doesn't pick up full quote for quote split in between br
		item['quotes'] = list()
		for res in response.xpath("//div[@class=\"quoteText\"]"):
			res = res.xpath('normalize-space(./text())').extract()[0].encode('ascii', "replace")[1:-1]
			item['quotes'].append(res)
		item['link'] = response.xpath('//a[@class=\"next_page\"]/@href').extract()
		yield item
		"""
		with open("gr_source", 'wb') as f:
			f.write(response.body)	
		
		for res in repsonse.xpath("//div[@class=\"quoteText\"]/text()").extract():
    			print res.encode("ascii", "replace")
		"""


		#item['quotes'].append(res.xpath('normalize-space(./text())').extract().encode("ascii", "replace")
		#item['quotes'] = response.xpath("//div[@class=\"quoteText\"]/text()").extract()
