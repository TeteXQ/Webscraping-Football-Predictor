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

    for index,row in matches.iterrows():
        homeTeam = Squad(row["Home"])
        awayTeam = Squad(row["Away"])

        if homeTeam.Rk == '1' or '2' or '3' or '4':
            homeTeamRkHilfe = 2
        elif homeTeam.Rk == '5' or '6' or '7' or '8':
            homeTeamRkHilfe = 1,5
        elif homeTeam.Rk == '9' or '10' or '11' or '12' or '13':
            homeTeamRkHilfe = 1,25
        else: homeTeamRkHilfe = 1
        
        if awayTeam.Rk == '1' or '2' or '3' or '4':
            awayTeamRkHilfe = 2
        elif awayTeam.Rk == '5' or '6' or '7' or '8':
            awayTeamRkHilfe = 1,5
        elif awayTeam.Rk == '9' or '10' or '11' or '12' or '13':
            awayTeamRkHilfe = 1,25
        else: awayTeamRkHilfe = 1
        
        homeTeam = Squad(row["Home"])
        awayTeam = Squad(row["Away"])
        homePred = round(float(homeTeamRkHilfe)*((homeTeam.xG)/(homeTeam.mp)))
        awayPred = round(float(awayTeamRkHilfe)*((awayTeam.xG)/(awayTeam.mp)))
        
        homeList.append(f"{homeTeam.name}")
        homePredGoalList.append(homePred)
        awayPredGoalList.append(awayPred)
        awayList.append(f"{awayTeam.name}")

        print(homeTeam.name, homeTeam.Rk, homeTeamRkHilfe)
        print('')
        print('VS')
        print('')
        print(awayTeam.name, awayTeam.Rk, awayTeamRkHilfe)

    list = [homeList,homePredGoalList,awayPredGoalList,awayList]

    df = pd.DataFrame(list,index=["Home","Homescore","Awayscore","Away"]).T
    return(df)



print(calculation_v1())

