# Eigene-API
Schnittstelle mit FLASK, Python realisieren

Schnittstelle mit FLASK erstellt und Wetterdaten sollen für zwei feste Orte ausgegeben werden.


############# Client Script ###################


import requests
import json

while True:
	city = raw_input("City? : ")
	url = 'http://127.0.0.1:5000/?q={}'.format(city)
	res = requests.get(url)
	data = res.json()

	if res.status_code == 200:
		print(data)

	break
  ############################################
  
  
  ############# API Script ###################
from flask import Flask, jsonify, request
app = Flask(__name__)
print "routes.py"
#Wetterdaten fuer Bonn und Darmstadt
darmstadt =    {
    "Darmstadt": {
        "Grad": 22,
        "Desc": "ohjjeee isch des heisss"
    }
}

bonn = {
    "Bonn": {
        "Grad": 43,
        "Desc": "grrrrr isch des kaaalt",
    }
}

weather = [{"Wetterdaten": {
    "Darmstadt": {
        "Grad": 22,
        "Desc": "ohjjeee isch des heisss",
           },
    "Bonn": {
        "Grad": 43,
        "Desc": "grrrrr isch des kaaalt",
    },
        }
}
]
#Ausgabe der Daten
@app.route('/', methods=['GET', 'POST'])
def hello():
    query = request.args.get('q', default = None, type = str)
    if (query is None) :
        return jsonify(weather)

    if (query.lower() == "darmstadt"):
        return jsonify(darmstadt)

    if (query.lower() == "bonn") :
        return jsonify(bonn)

    return jsonify(weather)
