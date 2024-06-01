import scrapy
from scrapy.http import Request
from zyte_coding_assignment.items import zyte2_1


class zyte21(scrapy.Spider):
    name = "zyte2_1"
    start_urls = ["https://books.toscrape.com/"]
    count = 0

    custom_settings = {
        'ITEM_PIPELINES': {
            'zyte_coding_assignment.pipelines.zyte_2_1_pipeline': 400
        }
    }



    def parse(self, response):
        print("-------------RESPONSE STARTED----------")
        urls = response.css('.side_categories .nav ul li a::attr(href)').getall()
        

        for link in urls:
            yield Request(url=self.start_urls[0]+link, callback=self.parse_books)

        print("-------------RESPONSE ENDED------------")

    def parse_books(self, response):
        print("-------------RESPONSE STARTED----------", response.url)
        item = zyte2_1()

        item['book_title'] = response.css('.product_pod .image_container a img::attr(alt)').getall()
        item['book_price'] = response.css('.product_pod .product_price p.price_color::text').getall()
        item['book_image_url'] = response.css('.product_pod .image_container a img::attr(src)').getall()
        item['book_details_page_url'] = response.css('.product_pod .image_container a::attr(href)').getall()

        for i in range(len(item['book_title'])):
            
            yield {
                    'book_title': item['book_title'][i],
                    'book_price': item['book_price'][i],
                    'book_image_url': item['book_image_url'][i],
                    'book_details_page_url': item['book_details_page_url'][i]
                }
            
            self.count += 1

            if self.count == 1000:
                self.crawler.engine.close_spider(self, 'Scraped 750 items')

        

        next_page = response.css('.pager .next a::attr(href)').get()
        if next_page:
            print(next_page, ' ', response.url)
            print(response.urljoin(next_page))
            yield Request(response.urljoin(next_page), callback=self.parse_books)


        print("-------------RESPONSE ENDED------------")
