from flask import Flask, render_template
from flask_googlemaps import GoogleMaps, Map, icons
import os

app = Flask(__name__)

GoogleMaps(app, key = "AIzaSyBLZbOLB1YcrTlXz_3_-yMgU6MG04wp5lU")

@app.route("/WashMobile")
def mapview():
    trdmap = Map(
        identifier="trdmap",
        lat=37.4419,
        lng=-122.1419,
        markers=[
            {
                'icon': icons.alpha.B,
                'lat':  37.4419,
                'lng':  -122.1419,
                'infobox': "Hello I am < b style='color:green;'>B< / b >!"
            },
            {
                'icon': icons.dots.blue,
                'lat': 37.4300,
                'lng': -122.1400,
                'infobox': "Hello I am < b style='color:blue;'>BLUE< / b >!"
            },
            {
                'icon': icons.dots.yellow,
                'lat': 37.4500,
                'lng': -122.1350,
                'infobox': (
                    "Hello I am < b style='color:#ffcc00;'> YELLOW < / b >!"
                    "< h2 >It is HTML title< / h2 >"
                    "< img src=' //placehold.it/50' >"
                    "< br >Images allowed!"
                )
            }
        ]
    )
    return render_template('map_templates.html', trdmap=trdmap)

# Template:
# in head:
#     {{trdmap.js}}
# in body:
#     {{trdmap.html}}

if __name__ == "__main__":
    app.run(debug=True)