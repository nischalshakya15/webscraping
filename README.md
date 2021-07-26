## WebScraping
Sample scrapy code to extract the data from various website. 

## Prerequisites 
* [Python 3.8](https://www.python.org/downloads/) 
* [Scrapy](https://docs.scrapy.org/en/latest/intro/install.html)

## Scrapying websites

### [PS4 Games](https://dlpsgame.net/category/ps4/) 
```python
scrapy crawl dlsps4 -o dlsps4.csv
```

### [British Council](https://ielts.britishcouncil.org/nepal/) 
```python
scrapy crawl britishcouncil -o britishcouncil.csv
```

### [Amazon](https://www.amazon.com/)
```python
scrapy crawl amazon -o amazon.csv
```

### [NEPSE](http://www.nepalstock.com/)

#### Prerequisites 
* MYSQL Server 

### Create database 
```sql 
create database nepse;
```

### Create the tables 
```sql 
create table todays_price
(
    id                bigint primary key not null auto_increment,
    traded_companies  varchar(255),
    no_of_transaction long,
    max_price         double,
    min_price         double,
    closing_price     double,
    traded_shares     double,
    amount            double,
    previous_closing  double,
    difference_rs     varchar(255),
    sn                bigint
);

create table floor_sheet
(
    id            bigint primary key not null auto_increment,
    sn            bigint,
    contract_no   bigint,
    stock_symbol  varchar(255),
    buyer_broker  bigint,
    seller_broker bigint,
    quantity      bigint,
    rate          double,
    amount        double
);

create table one_twenty_days_trading_average_price
(
    id                    bigint primary key auto_increment not null,
    sn                    bigint,
    stock_symbol          varchar(255),
    closing_average_price varchar(255),
    total_traded_amount   varchar(255),
    total_traded_shares   varchar(255),
    weighted_average      varchar(255),
    closing_price         varchar(255),
    closing_date          date
);

create table one_eighty_days_trading_average_price
(
    id                    bigint primary key auto_increment not null,
    sn                    bigint,
    stock_symbol          varchar(255),
    closing_average_price varchar(255),
    total_traded_amount   varchar(255),
    total_traded_shares   varchar(255),
    weighted_average      varchar(255),
    closing_price         varchar(255),
    closing_date          date
);

create table indices
(
    id                    bigint primary key auto_increment not null,
    sn                    bigint,
    nepse_index           double,
    absolute_change       double,
    percentage_change     varchar(255),
);
```

#### Scrap [Today's Share Price](http://www.nepalstock.com/todaysprice)
```python
scrapy crawl nepse -a nepse_data=todaysprice -o todaysprice.csv
```

#### Scrap [Today's Floor Sheet](http://www.nepalstock.com/floorsheet)
```python
scrapy crawl nepse -a nepse_data=floorsheet -o floorsheet.csv
```

#### Scrap [Datewise Indices](http://www.nepalstock.com/indices#)
```python
scrapy crawl nepse -a nepse_data=indices -o indices.csv
```

#### Scrap [120 Days Trading Average Price](http://www.nepalstock.com/calculation#)
```python
scrapy crawl nepse -a nepse_data=calculation -o calculation.csv
```

#### Scrap [180 Days Trading Average Price](http://www.nepalstock.com/calculationoneeighty)
```python
scrapy crawl nepse -a nepse_data=calculationoneeighty -o calculationoneeighty.csv
```

## Running the project
* Clone the repository. 
* Go to the root directory of the project using terminal or command line. 
* Execute the scrapy command line as show above

## References 
| Link | Type |
| ------|  --------- |
| [Change User Agent](https://www.simplified.guide/scrapy/change-user-agent)| Forbidden and captcha issue | 
| [Using Web Crawlers](https://www.datacamp.com/community/tutorials/making-web-crawlers-scrapy-python#project) | Reference | 
| [Python MYSQL](https://pynative.com/python-mysql-database-connection/) | Reference |