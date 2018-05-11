from bs4 import BeautifulSoup
import re
import requests
import csv
import pandas as pd
url = 'http://stats.espncricinfo.com/ci/engine/records/team/match_results_year.html?class=1;id=201;type=decade'
page = requests.get(url)
soup = BeautifulSoup(page.text,'html.parser')                                                 #parsing the very first page

counter = 0;


with open('matchnotes.csv', 'a') as csvFile:
 writer = csv.writer(csvFile)

 for a in soup.find_all('a',class_='QuoteSummary', href=True):
    s = ''
    s = s.join(['http://stats.espncricinfo.com',a['href']])                          #gets the url for each year table
    url = s
    followpage = requests.get(url)
    soupf = BeautifulSoup(followpage.text,'html.parser')                             #parses_each_year

    for a1 in soupf.find_all('a',class_='data-link', href=True):
                   randomstring = a1.get_text()
                   if(randomstring.startswith('Test')):                               #nowchange for odi or t20 tespectively                                    
                     list = []

                     flag = 0
                     p = ''
                     p = p.join(['http://stats.espncricinfo.com',a1['href']])
                     urlf = p
                     #list.append(urlf)
                     print('This is the link to the scorecard::',urlf)
                     ffollowpage = requests.get(urlf)
                     soupff = BeautifulSoup(ffollowpage.text,'html.parser')
                     
                     for a2 in soupff.find_all('li'):
                            matchnote = a2.get_text()
                            list = []
                            if(matchnote.find('Referral by') != -1):
                               if(matchnote.startswith('Day')):
                                  matchnote = matchnote[:5]
                                  print(matchnote,'\n')
                               else:
                                  print(matchnote,'\n')
                               list.append(urlf)
                               list.append(matchnote)
                               row = list
                               writer.writerow(row)
                               flag = 1
                            if(matchnote.find('Review by')!= -1):
                               if(matchnote.startswith('Day')):
                                  matchnote = matchnote[:5]
                                  print(matchnote,'\n')
                               else:
                                  print(matchnote,'\n')
                               list.append(urlf)
                               list.append(matchnote)
                               row = list
                               writer.writerow(row)
                               flag = 1
                     if(flag == 0):
                       print('drs was not used')
                       list.append(urlf)
                       list.append('DRS NOT USED')
                       row = list
                       writer.writerow(row)
            

 					 
                     
                     

                  
	
	
	
	

   
    
                  
    
    
    #for a3 in soupf.find_all('a',class_='data-link', href=True):         
    ##j = 0
    ##while j < totalloopcount: 
           ##print(soupf.find_all('a',class_= 'data-link',href=True)[j].get_text())
           ##j = j + 1









