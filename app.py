from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


@app.route('/')
def get_beer():
	r = requests.get('https://api.punkapi.com/v2/beers/random')
	beerson = r.json()

	beer = {
		'name': beerson[0]['name'],
		'abv': beerson[0]['abv'],
		'first_brewed': beerson[0]['first_brewed'],
		'description': beerson[0]['description'],
		'food_pairing': beerson[0]['food_pairing'][0],
		'yeast': beerson[0]['ingredients']['yeast']
	}

	return render_template('index.html', beer=beer)
