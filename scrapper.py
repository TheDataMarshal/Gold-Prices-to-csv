import requests
from bs4 import BeautifulSoup
from datetime import datetime
#import csv
import pandas as pd
import time

URL = "https://economictimes.indiatimes.com/commoditysummary/symbol-GOLD.cms"

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}

page = requests.get(URL, headers= headers)

soup = BeautifulSoup(page.content, "html.parser")
#print(soup.prettify())
def find_data():

    idsection = soup.find(id="MCX")
    Price_per_10_grams = idsection.find(class_='commodityPrice').get_text()
    #print(Price_per_10_grams)
    Time = datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S")
    #print(Time)
    #file = open('Gold_prices.csv', 'w')
    #writer = csv.writer(file)
    labels = ['timestamp', 'gold price per 10 grams']
    #writer.writerow(labels)
    #readfile = csv.reader(file)
    #writer.writerow([Time,Price_per_10_grams])
    #row = pd.DataFrame([Time],[Price_per_10_grams])
    #file.close()
    #print(readfile)
    data = {'timestamp': Time ,'gold price per 10 grams': Price_per_10_grams}
    existingfile = pd.read_csv('Gold_Prices.csv')
    update = existingfile.append(data,ignore_index = True )
    print(update)
    update.to_csv('Gold_prices.csv',columns =labels,index = False,date_format='%s')
    #print(existingfile)

while(True):
    find_data()
    time.sleep(1800)
