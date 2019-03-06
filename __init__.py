import random
from flask import Flask, render_template
from starwars import (get_films, get_planet, get_planets, get_ship, get_people)

app = Flask(__name__)

@app.route('/')
def index():
    context = {
        "films": get_films()['count'],
        "planets": get_planets()['results'],
        "planet_name": get_planet(1)['name'],
        "ship_length": get_ship(3)['length'],
        "ship_name": get_ship(3)['name'],
        "people": get_people()['results']
    }
    return render_template("index.html", **context)

if __name__ == "__main__":
    app.run(debug=True, port=8080, host='127.0.0.1')
