## WebScraping
Sample scrapy code to extract the data from various website. 

## Prerequisites 
* [Python 3.8](https://www.python.org/downloads/) 
* [Scrapy](https://docs.scrapy.org/en/latest/intro/install.html)

## Scrapying websites

### [PS4 Games](https://dlpsgame.net/category/ps4/) 
```python
scrapy crawl dlsps4 -0 dlsps4.csv
```

### [British Council](https://ielts.britishcouncil.org/nepal/) 
```python
scrapy crawl britishcouncil -0 britishcouncil.csv
```

### [Amazon](https://www.amazon.com/)
```python
scrapy crawl amazon -0 amazon.csv
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
