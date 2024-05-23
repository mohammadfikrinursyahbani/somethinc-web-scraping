# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


class SomethincItem(scrapy.Item):
    product_name = scrapy.Field(
        outputprocessor = TakeFirst(),
    )
    price = scrapy.Field(
        outputprocessor = TakeFirst()
    )
    benefit_product = scrapy.Field(
        outputprocessor = TakeFirst()
    )
    list_variant = scrapy.Field()
    description_product = scrapy.Field()
    how_to_use_product = scrapy.Field()
    quick_fact_product = scrapy.Field()
