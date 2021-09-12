import scrapy


class MarketdepthuserinputSpider(scrapy.Spider):
    name = 'marketdepthuserinput'
    allowed_domains = ['nepalstock.com']

    def __init__(self, symbol_number=None, **kwargs):
        super().__init__(name=None, **kwargs)
        self.symbol_number = symbol_number

    def start_requests(self):
        yield scrapy.Request(f'http://www.nepalstock.com/marketdepthofcompany/{self.symbol_number}/')

    def parse(self, response, **kwargs):
        full_market_name = response.xpath('//div[@id="home-contents"]/table/tr/td/div/text()').extract()
        print("Fetching the data of ", full_market_name[0])

        data = response.xpath('//div[@id="home-contents"]/table/tr/td/table[@class="depthIndex"]/tr/td')
        print(data)

        for d in data:
            heading = d.xpath('span/text()').extract()
            content = d.xpath('text()').extract()
            print(heading)
            print(content)

        pass
