import scrapy


class MarketdepthSpider(scrapy.Spider):
    name = 'marketdepth'
    allowed_domains = ['nepalstock.com']
    start_urls = ['http://www.nepalstock.com/marketdepth/']

    def parse(self, response, **kwargs):
        print('Processing URL ' + response.url)

        markets = response.xpath(
            '//select/option[@value]/text()'
        ).extract()
        print(markets)

        pass
