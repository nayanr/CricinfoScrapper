#code for getting match records of all the games




from bs4 import BeautifulSoup
import requests
import re
import csv
import pandas as pd


url = 'http://stats.espncricinfo.com/ci/engine/records/team/match_results_year.html?class=1;id=201;type=decade'
page = requests.get(url)
soup = BeautifulSoup(page.text,'html.parser')  

i = 0
for a in soup.find_all('a',class_='QuoteSummary', href=True):
    s = ''
    s = s.join(['http://stats.espncricinfo.com',a['href']])                          #gets the url for each year table
    url = s
    res = requests.get(url)
    soupf = BeautifulSoup(res.content,'lxml')
    table = soupf.find('table')
    df = pd.read_html(str(table))
    
    if(i==0):
       df[0].to_csv('2010.csv', index=False, encoding='utf-8')
    if(i==1):
       df[0].to_csv('2011.csv', index=False, encoding='utf-8')
    if(i==2):
       df[0].to_csv('2012.csv', index=False, encoding='utf-8')
    if(i==3):
       df[0].to_csv('2013.csv', index=False, encoding='utf-8')
    if(i==4):
       df[0].to_csv('2014.csv', index=False, encoding='utf-8')
    if(i==5):
       df[0].to_csv('2015.csv', index=False, encoding='utf-8')
    if(i==6):
       df[0].to_csv('2016.csv', index=False, encoding='utf-8')
    if(i==7):
       df[0].to_csv('2017.csv', index=False, encoding='utf-8')
    if(i==8):
       df[0].to_csv('2018.csv', index=False, encoding='utf-8')

    i = i + 1
