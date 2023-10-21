import requests
#import pandas as pd

def getDatafromSite():
    #URL of contest to scrape data from - here Bundesliga 1.
    contestURL = "https://fbref.com/en/comps/20/Bundesliga-Stats"

    #Download site
    data = requests.get(contestURL)
    data.text
    return data.text


print(getDatafromSite())