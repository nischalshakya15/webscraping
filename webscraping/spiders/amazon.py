import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/']

    def parse(self, response, **kwargs):
        print('Processing url ' + response.url)

        amazon_category_top = response.xpath('//div[@id = "gw-card-layout"]')

        print(amazon_category_top)

        for act in amazon_category_top:
            category = act.xpath(
                '//div[@class = "a-cardui-header"]/h2[@class = "a-color-base headline truncate-2line"]/text()'
            ).extract()
            print(category)

            link = act.xpath(
                '//div[@class = "a-cardui-footer"]/a[@class = "a-link-normal see-more truncate-1line"]/@href'
            ).extract()

            print(link)

            result = zip(category, link)

            yield result
