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
            self.mp = self.__mp()
    def __Home(self):
        #Does Squad play at home?
        try:
            df = matches
            if "Home" == df.columns[df.isin([self.name]).any()].any():
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
    def __mp(self):
        #Expected Goals Allowed on Home/Away 
        try:
            if self.home:
                df = leagueTable
                df = df[(df == self.name).any(axis=1)]
                return df["MP"].iloc[0]
            else:
                df = leagueTable
                df = df[(df == self.name).any(axis=1)]
                return df["MP"].iloc[0]
        except Exception as e:
            logging.error(f"Couldnt get Rank from {self.name}", e)
            return


def calculation_v1():
    matches = LeagueData.nextMatches()

    homeList = []
    homePredGoalList = []
    awayPredGoalList = []
    awayList = []

    dict = {1:2.5, 2:2.5, 3:2.5, 4:2, 5:2, 6:1.5, 7:1.5, 8:1.5, 9:1.25, 10:1.25, 11:1.25, 12:1.25, 13:1.25, 14:1, 15:1, 16:1, 17:1, 18:1}

    for index,row in matches.iterrows():
        homeTeam = Squad(row["Home"])
        awayTeam = Squad(row["Away"])

        homeTeamRkHilfe = dict[homeTeam.Rk]
        awayTeamRkHilfe = dict[awayTeam.Rk]

        homePred = round(float(homeTeamRkHilfe)*((homeTeam.xG)/(homeTeam.mp)))
        awayPred = round(float(awayTeamRkHilfe)*((awayTeam.xG)/(awayTeam.mp)))
        
        homeList.append(f"{homeTeam.name}")
        homePredGoalList.append(homePred)
        awayPredGoalList.append(awayPred)
        awayList.append(f"{awayTeam.name}")

        #print(homeTeam.name, homeTeam.Rk, homeTeamRkHilfe)
        #print('')
        #print('VS')
        #print('')
        #print(awayTeam.name, awayTeam.Rk, awayTeamRkHilfe)
    list = [homeList,homePredGoalList,awayPredGoalList,awayList]

    df = pd.DataFrame(list,index=["Home","Homescore","Awayscore","Away"]).T
    return(df)

print(calculation_v1())

