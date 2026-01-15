import scrapy
from ..items import AppItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes' #name of spider

    start_urls = [
        'https://quotes.toscrape.com/page/1/'
    ]

    page_number = 2
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

            # Pagination's concept
            next_page = r'https://quotes.toscrape.com/page/'+ str(QuoteSpider.page_number) +'/'
            # callback calls the parse function again
            if QuoteSpider.page_number < 11 :
                QuoteSpider.page_number = QuoteSpider.page_number + 1
                yield response.follow(next_page,callback = self.parse)
                
            yield appItem