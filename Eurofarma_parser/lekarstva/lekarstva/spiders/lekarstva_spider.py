import scrapy
from scrapy import Request
from scrapy import Selector
from scrapy.exceptions import CloseSpider
from datetime import date

from lekarstva.items import LekarstvaItem

class LekarstvaSpiderSpider(scrapy.Spider):
    name = 'lekarstva'
    allowed_domains = ['europharma.kz']
    start_urls = ['https://europharma.kz/catalog/lekarstvennye-sredstva?segment=available']

    def __init__(self, limit=10000, category_type='lekarstvennye-sredstva?', *args, **kwargs):
        super(LekarstvaSpiderSpider, self).__init__(*args, **kwargs)
        self.limit = int(limit)
        self.category_type = category_type
        self.count = 0



    def parse(self, response):
        links = response.css('.card-product__link::attr(href)').extract()
        for link in links:
            link = "https://europharma.kz" + link
            yield Request(url=link, callback=self.parse_detail_page)

        next_page = response.css('.pagination__item.next > .pagination__link::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_detail_page(self, response):
        if self.count >= self.limit:
            raise CloseSpider('limit reached')

        price = response.css('span.product__price-value::text').get()
        name = response.css('h1.product__title::text').get()
        url = response.url
        parseDate = date.today()

        item = LekarstvaItem()
        item['price'] = price
        item['name'] = name
        item['url'] = url
        item['parseDate'] = parseDate


        self.count += 1
        return item

