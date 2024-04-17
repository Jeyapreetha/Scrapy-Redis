
import scrapy
from scrapy_redis.spiders import RedisSpider
from example.items import QuoteItem

class QuotesSpider(RedisSpider):
    name = "example"
    redis_key = 'quotes_queue:start_urls'
    # Number of url to fetch from redis on each attempt
    redis_batch_size = 2
    # Max idle time(in seconds) before the spider stops checking redis and shuts down
    max_idle_time = 7
            
    def parse(self, response):
        for quote in response.css('div.quote'):
            item = QuoteItem()
            item['text'] =  quote.css('span.text::text').get()
            item['author'] =  quote.css('small.author::text').get()
            item['tags'] =  quote.css('div.tags a.tag::text').getall()
            yield item