from flask import Flask,jsonify,render_template
from flask_cors import CORS
import csv
import json 

app = Flask(__name__)
CORS(app)

def csv_to_geojson(csv_file):
    features = []
    with open(csv_file,'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            feature = {
                "type": "Feature",
                "properties": {
                    "name":row["Name"],
                    "type":row["Type"]
                },
                "geometry": {
                    "type": "Point",
                    "coordinates":[float(row["Lon"]),float(row["Lat"])]
                }
            }
            features.append(feature)
    geojson = {
        "type":"FeatureCollection",
        "features":features
    }

    return geojson

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/locations",methods=["GET"])
def get_locations():
    try:
        geojson_data = csv_to_geojson("locations.csv")
        return jsonify(geojson_data)
    except Exception as e:
        return jsonify({"error":str(e)}),500

if __name__=="__main__":
    app.run(debug=True,port=5000)