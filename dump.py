from bs4 import BeautifulSoup
from selenium import webdriver
import re
import os.path
from selenium.webdriver.support.ui import WebDriverWait
import time, datetime
import pandas as pd
from urllib.request import urlopen

url = "http://markets.cboe.com/us/equities/market_statistics/book/HSBC/"
url_tas = "https://quotes.freerealtime.com/quotes/HSBC/Time&Sales"
driver = webdriver.Firefox()
#driver_tas = webdriver.Firefox()
driver.get(url)
#driver_tas.get(url_tas)
file_path = "C:/Users/Abbas/Desktop/lob.csv"
file = open(file_path,"w")
file.write("Date,Time,AP5,AP4,AP3,AP2,AP1,AS5,AS4,AS3,AS2,AS1,BP5,BP4,BP3,BP2,BP1,BS5,BS4,BS3,BS2,BS1"+"\n")
file_path_tas = "C:/Users/Abbas/Desktop/tas_hsbc.csv"
file_tas = open(file_path_tas,"w")
file_tas.write("Date,Time,Price,Size"+"\n")
# if not(os.path.isfile(file_path)):
#
# else:
#     file = open(file_path, "r")

current_date = datetime.datetime.today().strftime('%d-%m-%Y')
until_date = '11-12-2018'

while True:
    if current_date == until_date:
        break
    time.sleep(6)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    #soup_tas = BeautifulSoup(driver_tas.page_source, "html.parser")
    #Quotes data
    ask_sizes = soup.find_all('td',{'class':'book-viewer__ask book-viewer__ask-shares'})
    ask_prices = soup.find_all('td',{'class':'book-viewer__ask book-viewer__ask-price book-viewer-price'})
    bid_sizes = soup.find_all('td',{'class':'book-viewer__bid book-viewer__bid-shares'})
    bid_prices = soup.find_all('td',{'class':'book-viewer__bid book-viewer__bid-price book-viewer-price'})
    ask_price5_time = soup.find('td',{'id':'ext-gen1057'})
    ask_price4_time = soup.find('td', {'id': 'ext-gen1060'})
    ask_price3_time = soup.find('td', {'id': 'ext-gen1063'})
    ask_price2_time = soup.find('td', {'id': 'ext-gen1066'})
    ask_price1_time = soup.find('td', {'id': 'ext-gen1069'})
    bid_price1_time = soup.find('td', {'id': 'ext-gen1072'})
    bid_price2_time = soup.find('td', {'id': 'ext-gen1075'})
    bid_price3_time = soup.find('td', {'id': 'ext-gen1078'})
    bid_price4_time = soup.find('td', {'id': 'ext-gen1081'})
    bid_price5_time = soup.find('td', {'id': 'ext-gen1084'})
    #Tas data
    # date_time = soup.find_all('td', {'id': re.compile('qmmt-tas-time-data-*')})
    # prices = soup.find_all('td', {'id': re.compile('qmmt-tas-price-data-*')})
    # sizes = soup.find_all('td', {'id': re.compile('qmmt-tas-volume-data-*')})
    trades_prices = soup.find_all('td',{'class':'book-viewer__trades-price'})
    trades_sizes = soup.find_all('td',{'class':'book-viewer__trades-shares'})
    if (ask_prices[0].text.strip() != "" and ask_sizes[0].text.strip() != ""):
        print("ask price1",ask_prices[0].text)
        print("ask size1",ask_sizes[0].text)
        print("bid price1",bid_prices[0].text)
        print("bid size1",bid_sizes[0].text)
        quote_time = ask_price5_time.text.strip() + ":350"
        file.write(current_date.strip()+","+quote_time+","+ask_prices[0].text.strip()+","+ask_prices[1].text.strip()+","+ask_prices[2].text.strip()+","+ask_prices[3].text.strip()+","+ask_prices[4].text.strip()+","
                   +ask_sizes[0].text.strip()+","+ask_sizes[1].text.strip()+","+ask_sizes[2].text.strip()+","+ask_sizes[3].text.strip()+","+ask_sizes[4].text.strip()+","
                   +bid_prices[0].text.strip()+","+bid_prices[1].text.strip()+","+bid_prices[2].text.strip()+","+bid_prices[3].text.strip()+","+bid_prices[4].text.strip()+","
                   +bid_sizes[0].text.strip()+","+bid_sizes[1].text.strip()+","+bid_sizes[2].text.strip()+","+bid_sizes[3].text.strip()+","+bid_sizes[4].text.strip()+"\n")

        #for i in range(0, len(trades_prices)):
        file_tas.write(current_date.strip()+","+quote_time+","+trades_prices[0].text+","+trades_sizes[0].text+"\n")
    else:
        print("Fetching failed")


file.close()
file_tas.close()

