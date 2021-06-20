import scrapy


class Dlsps4Spider(scrapy.Spider):
    name = 'dlsps4'
    allowed_domains = ['dlpsgame.net']
    start_urls = ['https://dlpsgame.net/category/ps4//']

    def parse(self, response, **kwargs):
        print('Processing URL : ' + response.url)
        ps4_game_title = response.xpath(
            '//div[@class = "post bar hentry"]/h2[@class = "post-title entry-title"]/a/text()').extract()
        current_page = response.xpath(
            '//div[@class = "wp-pagenavi"]/span[@class = "current"]/text()'
        ).extract()

        print("Processing page " + current_page[0])

        for item in ps4_game_title:

            yield {
                'title': item
            }

        next_page_number = response.xpath(
            '//div[@class = "wp-pagenavi"]/a[@class = "page larger"]/text()'
        ).extract()

        print(next_page_number)

        if next_page_number:
            abs_url = f'https://dlpsgame.net/category/ps4/page{next_page_number[0]}'
            yield scrapy.Request(
                url=abs_url,
                callback=self.parse
            )
        else:
            print()
            print('No page left')
            print()
