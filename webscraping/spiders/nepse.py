import scrapy


class NepseSpider(scrapy.Spider):
    name = 'nepse'
    allowed_domains = ['nepalstock.com']

    def __init__(self, nepse_data=None, **kwargs):
        super().__init__(name=None, **kwargs)
        self.nepse_data = nepse_data

    def start_requests(self):
        yield scrapy.Request(f'http://www.nepalstock.com/{self.nepse_data}/')

    def parse(self, response, **kwargs):
        print('Processing URL : ' + response.url)

        table_data = response.xpath(
            '//table/tr[not(@class)]'
        )

        if self.nepse_data == 'todaysprice':
            yield from self.extract_todays_price(table_data)
        if self.nepse_data == 'floorsheet':
            yield from self.extract_floor_sheet(table_data)
        if self.nepse_data == 'indices':
            yield from self.extract_indices(table_data)
        if self.nepse_data == 'calculation':
            yield from self.extract_one_twenty_days_trading_average_price(table_data)
        if self.nepse_data == 'calculationoneeighty':
            yield from self.extract_one_eighty_days_trading_average_price(table_data)

        current_page = response.xpath(
            '//div[@class = "pager"]/b/text()'
        ).extract()
        print(current_page)
        next_page = int(current_page[0]) + 1 if len(current_page) != 0 else 0
        print(next_page)

        if next_page != 0:
            if self.nepse_data == 'todaysprice':
                yield from self.extract_todays_price_pagination_data(next_page)
            if self.nepse_data == 'floorsheet':
                yield from self.extract_floor_sheet_pagination_data(next_page)
            if self.nepse_data == 'calculation':
                yield from self.extract_one_twenty_days_trading_average_price_pagination_data(next_page)
            if self.nepse_data == 'calculationoneeighty':
                yield from self.extract_one_eighty_days_trading_average_price_pagination_data(next_page)
        else:
            print()
            print('No page left')
            print()

    def extract_todays_price_pagination_data(self, next_page):
        next_url = f'http://www.nepalstock.com/main/todays_price/index/{next_page}/'
        yield scrapy.Request(
            url=next_url,
            callback=self.parse
        )

    @staticmethod
    def extract_todays_price(table_data):
        for td in table_data:
            row = td.xpath("td/text()").extract()
            print(row)

            removed_new_line = list(map(lambda tr: tr.strip(), row))
            filtered_empty_data = list(filter(lambda tr: tr != '', removed_new_line))
            size = len(filtered_empty_data)

            if size != 0 and size == 10:
                yield {
                    'S.N.': filtered_empty_data[0],
                    'Traded Companies': filtered_empty_data[1],
                    'No. Of Transaction': filtered_empty_data[2],
                    'Max Price': filtered_empty_data[3],
                    'Min Price': filtered_empty_data[4],
                    'Closing Price': filtered_empty_data[5],
                    'Traded Shares': filtered_empty_data[6],
                    'Amount': filtered_empty_data[7],
                    'Previous Closing': filtered_empty_data[8],
                    'Difference Rs': filtered_empty_data[9]
                }

    @staticmethod
    def extract_floor_sheet(table_data):
        for td in table_data:
            row = td.xpath("td/text()").extract()

            removed_new_line = list(map(lambda tr: tr.strip(), row))
            filtered_empty_data = list(filter(lambda tr: tr != '', removed_new_line))
            size = len(filtered_empty_data)
            if size != 0 and size == 8:
                yield {
                    'S.N.': filtered_empty_data[0],
                    'Contract No': filtered_empty_data[1],
                    'Stock Symbol': filtered_empty_data[2],
                    'Buyer Broker': filtered_empty_data[3],
                    'Seller Broker': filtered_empty_data[4],
                    'Quantity': filtered_empty_data[5],
                    'Rate': filtered_empty_data[6],
                    'Amount': filtered_empty_data[7]
                }

    def extract_floor_sheet_pagination_data(self, next_page):
        next_url = f'http://www.nepalstock.com/main/floorsheet/index/{next_page}/'
        yield scrapy.Request(
            url=next_url,
            callback=self.parse
        )

    @staticmethod
    def extract_indices(table_data):
        for td in table_data:
            row = td.xpath("td/text()").extract()

            removed_new_line = list(map(lambda tr: tr.strip(), row))
            filtered_empty_data = list(filter(lambda tr: tr != '', removed_new_line))
            size = len(filtered_empty_data)
            if size != 0 and size == 5:
                yield {
                    'S.N.': filtered_empty_data[0],
                    'Date': filtered_empty_data[1],
                    'NEPSE Index': filtered_empty_data[2],
                    'Absolute Change': filtered_empty_data[3],
                    'Percentage Change': filtered_empty_data[4]
                }

    @staticmethod
    def extract_one_twenty_days_trading_average_price(table_data):
        for td in table_data:
            row = td.xpath("td/text()").extract()

            removed_new_line = list(map(lambda tr: tr.strip(), row))
            filtered_empty_data = list(filter(lambda tr: tr != '', removed_new_line))
            size = len(filtered_empty_data)
            if size != 0 and size == 8:
                yield {
                    'S.N.': filtered_empty_data[0],
                    'Stock Symbol': filtered_empty_data[1],
                    'Closing Price Average': filtered_empty_data[2],
                    'Total Traded Amount': filtered_empty_data[3],
                    'Total Traded Shares': filtered_empty_data[4],
                    'Weighted Average': filtered_empty_data[5],
                    'Closing Price': filtered_empty_data[6],
                    'Closing Date': filtered_empty_data[7]
                }

    def extract_one_twenty_days_trading_average_price_pagination_data(self, next_page):
        next_url = f'http://www.nepalstock.com/main/calculation/index/{next_page}/'
        yield scrapy.Request(
            url=next_url,
            callback=self.parse
        )

    @staticmethod
    def extract_one_eighty_days_trading_average_price(table_data):
        for td in table_data:
            row = td.xpath("td/text()").extract()

            removed_new_line = list(map(lambda tr: tr.strip(), row))
            filtered_empty_data = list(filter(lambda tr: tr != '', removed_new_line))
            size = len(filtered_empty_data)
            if size != 0 and size == 8:
                yield {
                    'S.N.': filtered_empty_data[0],
                    'Stock Symbol': filtered_empty_data[1],
                    'Closing Price Average': filtered_empty_data[2],
                    'Total Traded Amount': filtered_empty_data[3],
                    'Total Traded Shares': filtered_empty_data[4],
                    'Weighted Average': filtered_empty_data[5],
                    'Closing Price': filtered_empty_data[6],
                    'Closing Date': filtered_empty_data[7]
                }

    def extract_one_eighty_days_trading_average_price_pagination_data(self, next_page):
        next_url = f'http://www.nepalstock.com/main/calculationoneeighty/index/{next_page}/'
        yield scrapy.Request(
            url=next_url,
            callback=self.parse
        )
