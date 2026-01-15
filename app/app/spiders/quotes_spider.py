import scrapy
from ..items import AppItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes' #name of spider

    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response):
        quote_div = response.css('div.quote')
        
        for data in quote_div:
            appItem = AppItem()
            quote = data.css('span.text::text').extract()
            author = data.css('small.author::text').extract()
            tags = data.css('a.tag::text').extract()

            appItem['quote'] = quote
            appItem['author'] = author
            appItem['tags'] = tags

            yield appItem