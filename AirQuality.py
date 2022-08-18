import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import date

url="https://www.iqair.com/iran/tehran"
html_data=requests.get(url).text

soup=BeautifulSoup(html_data,'html.parser')

tehran_pollution_data=pd.DataFrame(columns=["Date","Air pollution level","Air quality index","Main pollutant"])
for row in soup.find_all('tbody')[3].find_all('tr'):
    col=row.find_all('td')
    apl=col[0].text
    aqi=col[1].text
    mp=col[2].text
    tehran_pollution_data=tehran_pollution_data.append({"Date":date.today(),"Air pollution level":apl,"Air quality index":aqi,"Main pollutant":mp},ignore_index=True)
    
    import csv
from os import path
file_status = path.isfile('AirQuality.csv') 

with open('AirQuality.csv', 'a+', newline='') as csvfile:
    fieldnames = ["Date", "Air pollution level","Air quality index","Main pollutant"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    if not file_status:
        writer.writeheader() 
    writer.writerow({"Date":date.today(),"Air pollution level":apl,"Air quality index":aqi,"Main pollutant":mp})
