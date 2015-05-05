import scrapy
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from goodreads.items import GrItem

# Good Reads quote spider 
class GrSpider(CrawlSpider):
	name = "gr"
	allowed_domains = ["goodreads.com"]
	start_urls = [
		"https://www.goodreads.com/quotes/tag/love"
	]
	#recursively go through all pages with quotes
	rules = (Rule (SgmlLinkExtractor(allow=('/quotes/tag/love?page',))
	, callback="parse", follow= True),
    	)

	def parse(self, response):
		item = GrItem() 
		#doesn't pick up full quote for quote split in between br
		item['quotes'] = list()
		for res in response.xpath("//div[@class=\"quoteText\"]"):
			res = res.xpath('normalize-space(./text())').extract()[0].encode('ascii', "replace")[1:-1]
			item['quotes'].append(res)
		item['link'] = response.xpath('//a[@class=\"next_page\"]/@href').extract()
		yield item
