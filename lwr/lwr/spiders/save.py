import scrapy
import html5lib
from bs4 import BeautifulSoup
import re
import os


os.system("rm ./log_file.txt")

class MySpider(scrapy.Spider):
    name = "wikicrawler"
    allowed_domains = ["https://en.wikipedia.org"]
    start_urls = [
        "https://en.wikipedia.org/wiki/List_of_terrorist_incidents_in_2016"
    ]

    def __init__(self):
        self.log_file = open('log_file.txt', 'w')

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html5lib')
        container = soup.find(id="mw-content-text")
        first_list = container.find("ul").find_all("li")

        for item in first_list:
            link = item.find('a').get("href")
            month = re.search(r'(?<=in_)(\w*)(?=_)', link).group()
            year = re.search(r'2(\w*)$', link).group()
            url = self.allowed_domains[0] + link



            # self.log_file.write(month + ",  " + year + ",  " + url + ", \n")

            request = scrapy.Request(url, callback=self.parse_months, dont_filter=True)
            request.meta['month'] = month
            request.meta['year'] = year
            request.meta['url'] = url
            yield request


    def parse_months(self,response):

        soup = BeautifulSoup(response.text, 'html5lib')
        table = soup.find(class_="wikitable sortable")


        rows = table.find_all("tr")
        column_names_th = rows[0].find_all("th")

        column_names = list()
        for col in column_names_th:
            column_names.append(col.string)

        iter_rows = iter(rows)
        next(iter_rows)


        for row in iter_rows:
            #test = LwrItem()
            self.log_file.write(str(row))

            # class LwrItem(scrapy.Item):
            #     # define the fields for your item here like:
            #     month = scrapy.Field()
            #     year = scrapy.Field()
            #     url = scrapy.Field()
            #     day = scrapy.Field()
            #     type = scrapy.Field()
            #     dead = scrapy.Field()
            #     injured = scrapy.Field()
            #     location = scrapy.Field()
            #     details = scrapy.Field()
            #     perpetrator = scrapy.Field()
            #     source = scrapy.Field()




                #for row in rows:
        #    columns = row.find_all("td")

        # self.log_file.write(str(column_names))

