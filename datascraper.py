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

    

a = getTablesfromSite("https://fbref.com/en/comps/20/Bundesliga-Stats")
b = selectTablefromTables(a,1)
print(b)
#print(list(b.columns))
#c = removeIllegalChars(b)
#print(c)