# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LekarstvaItem(scrapy.Item):
    price = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    parseDate = scrapy.Field()

    # name = scrapy.Field()
    pass
