# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class zyte_2_1_pipeline:
    def process_item(self, item, spider):

        item['book_price'] = item["book_price"].replace('£', '')
        item['book_image_url'] = "https://books.toscrape.com/" + item["book_image_url"].replace('../', '')
        item['book_details_page_url'] = "https://books.toscrape.com/catalogue/" + item["book_details_page_url"].replace('../', '')
        return item
        
        
    
    
