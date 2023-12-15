import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class RhymesSpider(CrawlSpider):
    name = 'nursery_rhymes_spider'
    allowed_domains = ["allnurseryrhymes.com"]
    start_urls = ['https://allnurseryrhymes.com']
    rules = (
        Rule(LinkExtractor(allow=('/')), follow=True, callback='parse_items'),
    )
    
    def parse_items(self, response): 
        entry_content = response.css('div.entry-content').get()
        yield {
                'page_url': response.url,
                'entry_content': entry_content,
            }

        next_page = response.css('a::attr(href)').get() 
        if next_page and next_page != '#content':
            yield scrapy.Request(url=next_page, callback=self.parse_items) 