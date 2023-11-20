import datascraper
import pandas as pd
import numpy as np
import logging

#Temporary version of defining tables
LeagueData = datascraper.LeagueData("https://fbref.com/en/comps/20/Bundesliga-Stats")
matches = LeagueData.nextMatches()
leagueTable = LeagueData.getLeagueTable()
leagueTableHomeAway = LeagueData.getTableHomeAway()


class Squad:
    def __init__(self, squadName:str):
        self.name = squadName
        self.home = self.__Home()
        if self.home is not None:
            self.Rk = self.__Rk()
            self.xG = self.__xG()
            #self.xGA = self.__xGA()

    def __Home(self):
        #Does Squad play at home?
        try:
            df = matches
            if "Home" == df.columns[df.isin([self.name]).any()]:
                return True
            elif "Away" == df.columns[df.isin([self.name]).any()]:
                return False
        except Exception as e:
            logging.error(f"Coudnt find Squad {self.name}", e)
            return
    def __Rk(self):
        #Rank of Squad
        try:
            df = leagueTable
            df = df[(df == self.name).any(axis=1)]
            return df["Rk"].iloc[0]
        except Exception as e:
            logging.error(f"Couldnt get Rank from {self.name}", e)
            return
    def __xG(self):
        #Expected Goals depending on Home/Away
        try:
            if self.home:
                df = leagueTableHomeAway
                df = df[(df == self.name).any(axis=1)]
                return df["Home","xG"].iloc[0]
            else:
                df = leagueTableHomeAway
                df = df[(df == self.name).any(axis=1)]
                return df["Away","xG"].iloc[0]
        except Exception as e:
            logging.error(f"Couldnt get expected Goals from {self.name}", e)
            return
    def __xGA(self):
        #Expected Goals Allowed on Home/Away
        try:
            if self.home:
                df = leagueTableHomeAway
                df = df[(df == self.name).any(axis=1)]
                return df["Home","xGA"].iloc[0]
            else:
                df = leagueTableHomeAway
                df = df[(df == self.name).any(axis=1)]
                return df["Away","xGA"].iloc[0]
        except Exception as e:
            logging.error(f"Couldnt get Rank from {self.squad}", e)
            return


bayern = Squad("Bayern Munich")
print(bayern.home)
print(bayern.Rk)
print(bayern.xG)
