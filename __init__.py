import random
from flask import Flask, render_template
from starwars import (get_films, get_planet, get_planets, get_ship, get_people)

app = Flask(__name__)

@app.route('/')
def index():
    context = {
        "films": get_films()['count'],
        "planets": get_planets()['results'],
        "people": get_people()['results'],
        "both": get_planets()['results'] + get_people()['results'],
    }
    return render_template("index.html", **context, )


@app.route('/people_planet_details/<int:planet_id>')
def people_planet_details(person_id, planet_id):
    details = get_planet(planet_id)['name']
    return render_template("people.html", details=details)

if __name__ == "__main__":
    app.run(debug=True, port=8080, host='127.0.0.1')
