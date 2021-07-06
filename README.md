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
