from bs4 import BeautifulSoup
import re
import requests
import csv
import pandas as pd


url = 'http://stats.espncricinfo.com/ci/engine/records/team/match_results_year.html?class=1;id=201;type=decade'
page = requests.get(url)
soup = BeautifulSoup(page.text,'html.parser')                                                 #parsing the very first page
listofyear = []                                                                               #lists for final output files
listoflinks = []
listoflinktoscorecardsofgamesinaparticularyear = []

for a in soup.find_all('a',class_='QuoteSummary', href=True):
    s = ''
    stringofyear = a.get_text()                                                      #gets the year
    listofyear.append(stringofyear)                                                  #feedsitintoalist
    s = s.join(['http://stats.espncricinfo.com',a['href']])                          #gets the url for each year table
    url = s
    listoflinks.append(url)                                                          #feedsitintoalist
    


    followpage = requests.get(url)
    soupf = BeautifulSoup(followpage.text,'html.parser')                             #parses_each_year
    for a1 in soupf.find_all('a',class_='data-link', href=True):
                   randomstring = a1.get_text()
                   if(randomstring.startswith('Test')):                               #nowchange for odi or t20 tespectively
                     p = ''
                     p = p.join(['http://stats.espncricinfo.com',a1['href']])
                     urlf = p
                     listoflinktoscorecardsofgamesinaparticularyear.append(urlf)
                     
df = pd.DataFrame({'URL OF THE SCORECARDS OF GAMES FROM 2010 TO 2018' : listoflinktoscorecardsofgamesinaparticularyear})
df.to_csv('links_to_all_scorecards_test_games_taken_over_the_decade.csv', index=False, encoding='utf-8')

df = pd.DataFrame({'Year' : listofyear, 'Url to all the games held in the year' : listoflinks})
df.to_csv('linkstoallgamesinayear.csv', index=False, encoding='utf-8')






