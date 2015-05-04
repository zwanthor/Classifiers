
BOT_NAME = 'goodreads'

SPIDER_MODULES = ['goodreads.spiders']
NEWSPIDER_MODULE = 'goodreads.spiders'

ITEM_PIPELINES = {
	'goodreads.pipelines.JsonWriterPipeline': 400,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'goodreads (+http://www.yourdomain.com)'
