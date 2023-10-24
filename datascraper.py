import pandas as pd
import logging
import numpy as np
#import requests
#from bs4 import BeautifulSoup

def getTablesfromSite(contestURL):
    #Get all tables of given Site
    try:
        allTables = pd.read_html(contestURL)
        logging.info(f"Found {len(allTables)} tables on {contestURL}")
        return allTables
    except Exception as e:
        logging.error(f"Couldnt find any tables on {contestURL}", e)
        return None
        
def selectTablefromTables(Tables, pos:int):
    #Select one of the tables from site 
    try:
        specificTable = Tables[pos]
        logging.info(f"Selected 1 table from {len(Tables)}")
        return specificTable
    except Exception as e:
        logging.error(f"Couldnt select any Tables from given value", e)
        return None
    
def removeIllegalChars(Table):
    try:
        df = Table
        df = df.replace(("'")," ")
        return df
    except Exception as e:
        logging.error(f"Couldnt change illegal chars", e)
        return None

def getUpcomingMatchday(contestURL):
    try:
        df = pd.read_html(contestURL)[0]
        try:
            #Get rid of unneeded columns
            df = df.drop(["Attendance", "Referee","Match Report", "Notes"], axis=1)
            #Delete all rows except the ones from next / current matchday
            df = df[df['Score'].isnull()].dropna(axis = 0, how = 'all')
            df = df[df["Wk"].iloc[0] >= df["Wk"]]
            return df
        except Exception as e:
            logging.error(f"Couldnt format Dataframe properly \n {df}", e)
    except Exception as e:
        logging.error(f"Couldnt find any tables on given URL {contestURL}", e)
        return None

def getLeagueTable(contestURL):
    try:
        df = selectTablefromTables(getTablesfromSite(contestURL),0)
        return df
    except Exception as e:
        logging.error(f"Couldnt get Leaguetable from {contestURL}", e)
        return


#a = getTablesfromSite("https://fbref.com/en/comps/20/Bundesliga-Stats")
d = getUpcomingMatchday("https://fbref.com/en/comps/20/schedule/Bundesliga-Scores-and-Fixtures")
g = getLeagueTable("https://fbref.com/en/comps/20/Bundesliga-Stats")
#b = selectTablefromTables(a,1)
print(g)
print(d)
#print(b)
#print(list(b.columns))
#c = removeIllegalChars(b)
#print(c)