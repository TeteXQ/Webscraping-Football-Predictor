from flask import Blueprint, render_template, redirect, url_for

pages = Blueprint(__name__, "pages")

@pages.route("/")
def home():
    return render_template("index.html") #nimmt daten aus der html datei aus dem ordner templates

@pages.route("/predictions")
def predictions():
    return render_template("predictions.html")

@pages.route("/calculations")
def predictions():
    return render_template("calculations.html")