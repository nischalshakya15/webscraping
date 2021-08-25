import scrapy


class MarketdepthSpider(scrapy.Spider):
    name = 'marketdepth'
    allowed_domains = ['nepalstock.com']
    start_urls = ['http://www.nepalstock.com/marketdepth/']

    def parse(self, response, **kwargs):
        print('Processing URL ' + response.url)

        choose_symbols = response.xpath(
            '//div[@class="col-xs-12 col-md-8 col-sm-12"]/form/div[@class="form-group"]/select['
            '@id="StockSymbol_Select"]/option[@value != ""]'
        )

        for choose_symbol in choose_symbols:
            market = choose_symbol.xpath('text()').extract()
            symbol_number = choose_symbol.xpath('@value').extract()

            yield {
                'symbol_number': symbol_number[0],
                'market': market[0]
            }
