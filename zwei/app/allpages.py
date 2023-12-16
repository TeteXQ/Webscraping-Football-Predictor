from flask import Blueprint, render_template, redirect, url_for

pages = Blueprint("pages", '__name__')

@pages.route("/index.html")
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
    return render_template("current_chart.html")

@pages.route("/current_matchday")
def current_matchday():
    return render_template("current_matchday.html")