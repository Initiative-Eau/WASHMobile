from flask import Flask, render_template
from flask_googlemaps import Map, icons
import os

app = Flask(__name__)

class WaterSource:
    def __init__(selfself, key , name, lat, lng):
        self.key = key
        self.name = name
        self.lat = lat
        self.lng = lng

FadaNgourma = (
    WaterSource('FADS79', 'FADS79', 12.068236, 0.353520)
)
FadaNgourma_by_key = {watersource.key: watersource for watersource in FadaNgourma}

@app.route("/WashMobile/home")
def home():
    return render_template('home.html')

# @app.route("/WashMobile/about")
# def about():
#     return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)