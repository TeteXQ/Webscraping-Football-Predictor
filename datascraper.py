import pandas as pd
import logging
import numpy as np
import requests
from bs4 import BeautifulSoup



class LeagueData:

    def __init__(self, contestURL:str):
        self.contestURL = contestURL
        pass

    def switchURL(self, keyword:str):
            try:
                res = requests.get(self.contestURL)
                soup = BeautifulSoup(res.content, "html.parser")
                partialURL = soup.select(f"a[href*={keyword}]")[0].get("href")
                logging.info(f"Found {partialURL} from keyword: {keyword}")
                return("/".join(self.contestURL.split("/",maxsplit=3)[:3])+partialURL)
            except Exception as e:
                logging.error(f"Couldnt find any URLs from keyword: {keyword}", e)
    
    def getTablesfromSite(self):
        #Get all tables of given Site
        try:
            allTables = pd.read_html(self.contestURL)
            logging.info(f"Found {len(allTables)} tables on {self.contestURL}")
            return allTables
        except Exception as e:
            logging.error(f"Couldnt find any tables on {self.contestURL}", e)
            return None
         
    def selectTablefromTables(self, Tables, pos:int):
        #Select one of the tables from site 
        try:
            specificTable = Tables[pos]
            logging.info(f"Selected 1 table from {len(Tables)}")
            return specificTable
        except Exception as e:
            logging.error(f"Couldnt select any Tables from given value", e)
            return None
    
    def removeIllegalChars(self,Table):
        try:
            df = Table
            df = df.replace(("'")," ")
            return df
        except Exception as e:
            logging.error(f"Couldnt change illegal chars", e)
        return None
    
    def nextMatchday(self):
        try:
            scoresURL = self.switchURL("Scores-and-Fixtures")
            df = pd.read_html(scoresURL)[0]
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
            logging.error(f"Couldnt find any tables on given URL {self.contestURL}", e)
            return None

    def currentMatchday(self):
        try: 
            scoresURL = self.switchURL("Scores-and-Fixtures")
            df = pd.read_html(scoresURL)[0]
            dfnextMD = self.nextMatchday()
            df = df[df["Wk"].isin(dfnextMD["Wk"])]
            logging.info(f"Successfully found current matchday")
            return df
        except Exception as e:
            logging.error(f"Couldnt generate current matchday",e)
            return

    def getLeagueTable(self):
        try:
            df = self.selectTablefromTables(LeagueData.getTablesfromSite(),0)
            return df
        except Exception as e:
            logging.error(f"Couldnt get Leaguetable from {self.contestURL}", e)
            return



d = LeagueData("https://fbref.com/en/comps/20/Bundesliga-Stats")
#print(d.nextMatchday())
print(d.getLeagueTable())

#print(g)