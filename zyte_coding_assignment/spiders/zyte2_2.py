import scrapy
from scrapy_splash import SplashRequest

class zyte22(scrapy.Spider):
    name = 'zyte2_2'

    start_urls = ['http://quotes.toscrape.com/js/']


    custom_settings = { 
        'FEEDS': {'quotes.csv': {'format': 'csv', 'overwrite': False}} 
    } 

    def start_requests(self):
        yield SplashRequest("http://quotes.toscrape.com/js/", self.parse,args={'wait': 5})

    def parse(self, response):
        print("______________________________________________________________")
        print(response)
        print("________________________________------------------------------")
        for quote in response.css('div.quote'):
            print(quote.css('span.text::text').get())
            print(quote.css('span small.author::text').get())
            print(quote.css('div.tags a.tag::text').getall())
            yield {
                'quote': quote.css('span.text::text').get(),
                'author': quote.css('span small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
