import scrapy
import html5lib
from bs4 import BeautifulSoup
import re
import os
from lwr.items import LwrItem

os.system("rm ./log_file.txt")
os.system("rm ./attacks.json")

class MySpider(scrapy.Spider):
    name = "wikicrawler"
    allowed_domains = ["https://en.wikipedia.org"]
    start_urls = [
        "https://en.wikipedia.org/wiki/List_of_terrorist_incidents_in_November_2016"
    ]

    def __init__(self):
        self.log_file = open('log_file.txt', 'w')


    def parse(self, response):




    def parse_pages(self, response):
        soup = BeautifulSoup(response.text, 'html5lib')

        print(response.meta['page'])

        # # Get year from title as it is more reliable
        # title = soup.find('title').string
        # year = re.search(r'(\d{4})', title).group()
        #
        #
        # tables = soup.find_all(class_="wikitable sortable")
        #
        # for table in tables:
        #
        #     # For each table get the id with the hopes of identifying the year and month of info
        #     table_id = table.get('id')
        #     # This looks for the month. not so robust
        #     month = re.search(r'(?<=\d{4})(\w*)', table_id).group()
        #
        #
        #     # add information to get year of event
        #
        #     # Get's all column tags.
        #     rows = table.find_all("tr")
        #     column_names_th = rows[0].find_all("th")
        #
        #     # Extracts the text from column tags
        #     column_names = list()
        #     for col_name in column_names_th:
        #         # replace removes '-' and ' ' because it's not good for varnames
        #         list.append(column_names, col_name.text.replace('-','').replace(' ','') )
        #
        #
        #
        #     # Skips the header row
        #     iter_rows = iter(rows)
        #     next(iter_rows)
        #
        #     for row in iter_rows:
        #         attack = LwrItem()
        #         cells = row.find_all('td')
        #
        #
        #
        #         # must make our thing robust to each column. run as normal unless special
        #         for cell, col_name in zip(cells, column_names):
        #
        #             # Deal with location information
        #             if (col_name == "Location"):
        #                 links = cell.find_all('a')
        #                 place = ''
        #
        #                 #to skip the first link which is an image create an iterable
        #                 iter_links = iter(links)
        #                 next(iter_links)
        #
        #                 for link in iter_links:
        #                     place += str(link.string) + " "
        #                 attack[col_name] = place
        #
        #             # Deal with State or NonState weirdness
        #             elif(col_name == "State" or col_name == "Nonstate"):
        #                 image_tag = cell.find('img')
        #
        #                 if image_tag is None:
        #                     attack[col_name] = 0
        #                 else:
        #                     attack[col_name] = 1
        #
        #             # Deal with okay/everything else things
        #             else:
        #                 #self.log_file.write(str(col_name) + str(cell.string) + "\n shit \n")
        #                 attack[str(col_name)] = cell.text
        #
        #         attack['Year'] = year
        #         attack['Month'] = month
        #         yield attack
