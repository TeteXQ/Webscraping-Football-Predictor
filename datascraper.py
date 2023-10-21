import requests
from bs4 import BeautifulSoup
import pandas as pd

def getDatafromSite():
    #URL of contest to scrape data from - here Bundesliga 1.
    contestURL = "https://fbref.com/en/comps/20/Bundesliga-Stats"

    #Find tables
    data = requests.get(contestURL)
    soup = BeautifulSoup(data.text, features="html.parser")
    statsTable = soup.select("table.stats_table")
    links = statsTable.find_all("a")
    links = [l.get("href") for l in links]
    


    #asdfgihaysdfljökghydfg

    return statsTable
print(getDatafromSite())