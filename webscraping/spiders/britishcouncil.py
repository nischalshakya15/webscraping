import scrapy


class BritishcouncilSpider(scrapy.Spider):
    name = 'britishcouncil'
    allowed_domains = ['ielts.britishcouncil']
    start_urls = ['http://ielts.britishcouncil.org/nepal/']

    def parse(self, response, **kwargs):
        print("Processing URL " + response.url)

        ul_path = response.xpath('//ul[@class = "menu2"]/li/a/span/text()').extract()
        ul_link = response.xpath('//ul[@class = "menu2"]/li/a/@href').extract()

        items = zip(ul_path, ul_link)

        for item in items:
            yield {
                'category': item[0],
                'link': "https://ielts.britishcouncil.org/" + item[1]
            }
