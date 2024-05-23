import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import SomethincItem
from scrapy.loader import ItemLoader

class ProductsSpider(CrawlSpider):
    name = "products"
    allowed_domains = ["somethinc.com"]
    start_urls = ["https://somethinc.com/en/product/"]

    rules = (
        Rule(LinkExtractor(allow=(r"detail",)), callback="parse_item"),
    )

    def parse_item(self, response):
        l = ItemLoader(item=SomethincItem(), response=response)
        l.add_css("product_name", "h1.title::text")
        l.add_css("price", "div.price s::text")
        l.add_css("benefit_product", "div.text-lh::text")
        l.add_css("list_variant", "div.select-overlay-variant::text")
        l.add_css("description_product", "div.products-detail-info-text div.col-lg-17 span::text")
        l.add_css("how_to_use_product", "div.products-detail-info-text col-xl-10 span::text")
        l.add_css("quick_fact_product", "div.products-detail-info-text ul::text")
        return l.load_item()
    
