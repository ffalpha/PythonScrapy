import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['https://github.com/trembacz/xpath-finder']

    def parse(self, response):
        title = response.css(
            '.text-normal').extract
        print(title)
