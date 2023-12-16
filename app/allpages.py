from flask import Blueprint, render_template, redirect, url_for

import pandas as pd
from footballdata.datascraper import LeagueData

league = LeagueData("https://fbref.com/en/comps/20/Bundesliga-Stats")


pages = Blueprint("pages", '__name__')

@pages.route("/")
def home():
    return render_template("index.html") #nimmt daten aus der html datei aus dem ordner templates

@pages.route("/predictions")
def predictions():
    return render_template("predictions.html")

@pages.route("/history")
def history():
    return render_template("history.html")

@pages.route("/current_chart")
def current_chart():
    df = league.getLeagueTable().drop(["Pts/MP","xGD/90","Attendance"], axis=1)
    return render_template("current_chart.html", column_names=df.columns.values, row_data=list(df.values.tolist()), zip=zip)

@pages.route("/current_matchday")
def current_matchday():
    df = league.currentMatchday().drop(["Wk","Day","Date","Time","Attendance","Venue","Referee"], axis=1)
    return render_template("current_matchday.html", column_names=df.columns.values, row_data=list(df.values.tolist()), zip=zip)