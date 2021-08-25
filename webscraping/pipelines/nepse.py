import mysql.connector

from mysql.connector import Error


class NepsePipeline(object):

    def __init__(self):
        db = 'nepse'
        host = 'localhost'
        port = 3306
        user = 'root'
        password = 'root'

        try:
            self.connection = mysql.connector.connect(host=host, port=port, db=db, user=user, passwd=password)
            self.cursor = self.connection.cursor()
        except Error as e:
            print("Error while connecting to MYSQL ", e)

    def process_item(self, item, spider):

        if spider.name == 'marketdepth':
            item_list = list(item.values())
            try:
                insert_query = """
                           INSERT INTO market_depth(stock_symbol, stock_name) VALUES (%s, %s)
                       """
                cursor = self.connection.cursor()
                cursor.execute(insert_query, item_list)
                self.connection.commit()

                print(cursor.rowcount, " Record insert successfully.")
            except Error as e:
                print("Error while executing queries ", e)

        if spider.name == 'nepse':
            nepse_argument = spider.nepse_data
            insert_query = ""
            item_list = list(item.values())
            try:
                if nepse_argument == 'todaysprice':
                    insert_query = """
                                            INSERT INTO todays_price (sn, traded_companies, no_of_transaction, max_price, min_price,
                                            closing_price, traded_shares, amount, previous_closing, difference_rs) 
                                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                        """

                if nepse_argument == 'indices':
                    insert_query = """
                                            INSERT INTO indices (sn, date, nepse_index, absolute_change, percentage_change) 
                                            VALUES (%s, %s, %s, %s, %s)
                                        """

                if nepse_argument == 'calculation':
                    insert_query = """
                                            INSERT INTO one_twenty_days_trading_average_price (sn, stock_symbol, 
                                            closing_average_price, total_traded_amount, total_traded_shares, weighted_average, 
                                            closing_price, closing_date) 
                                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                                        """

                if nepse_argument == 'calculationoneeighty':
                    insert_query = """
                                            INSERT INTO one_eighty_days_trading_average_price (sn, stock_symbol, 
                                            closing_average_price, total_traded_amount, total_traded_shares, weighted_average, 
                                            closing_price, closing_date) 
                                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                                            """

                if nepse_argument == 'floorsheet':
                    insert_query = """
                                INSERT INTO floor_sheet (sn, contract_no, stock_symbol, buyer_broker, seller_broker, quantity, 
                                rate, amount) 
                                values (%s, %s, %s, %s, %s, %s, %s, %s)
                            """

                cursor = self.connection.cursor()
                cursor.execute(insert_query, item_list)
                self.connection.commit()

                print(cursor.rowcount, "Record insert successfully")
            except Error as e:
                print("Error while executing queries ", e)
