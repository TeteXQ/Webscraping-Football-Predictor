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
            self.xGDp90 = self.__xGDp90()
            self.xG = self.__xG()
            self.xGA = self.__xGA()

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
    def __xGDp90(self):
        #Expected Goals depending on Home/Away divided by the amount of matches
        try:
            if self.home:
                df = leagueTableHomeAway
                df = df[(df == self.name).any(axis=1)]
                return df["Home","xGD/90"].iloc[0]
            else:
                df = leagueTableHomeAway
                df = df[(df == self.name).any(axis=1)]
                return df["Away","xGD/90"].iloc[0]
        except Exception as e:
            logging.error(f"Couldnt get expected Goals per 90 from {self.name}", e)
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
            logging.error(f"Couldnt get Rank from {self.name}", e)
            return
        

def TestCalculation():
    matches = LeagueData.nextMatches()

    homeList = []
    homePredList = []
    awayPredList = []
    awayList = []

    for index,row in matches.iterrows():
        #print(row["Home"])
        homeTeam = Squad(row["Home"])
        awayTeam = Squad(row["Away"])
        homePred = float(homeTeam.Rk)*((homeTeam.xG)/(awayTeam.xGA))
        awayPred = float(awayTeam.Rk)*((awayTeam.xG)/(homeTeam.xGA))
        
        homeList.append(f"{homeTeam.name}")
        homePredList.append(homePred)
        awayPredList.append(awayPred)
        awayList.append(f"{awayTeam.name}")
        print (homeTeam.name)
        print (homeTeam.xGA)
        print (awayTeam.name)
        print (awayTeam.xG)

    list = [homeList,homePredList,awayPredList,awayList]

    df = pd.DataFrame(list,index=["Home","Homescore","Awayscore","Away"]).T
    return(df)




print(matches)
print(TestCalculation())
glad = Squad("M'Gladbach")
print(glad.name)
