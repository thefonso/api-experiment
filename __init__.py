import random
from flask import Flask, render_template
from starwars import (get_films, get_planet, get_planets, get_ship, get_people)
from collections import defaultdict

app = Flask(__name__)

l1 = [{"index":1, "b":2}, {"index":2, "b":3}, {"index":3, "green":"eggs"}]
l2 = [{"index":1, "c":4}, {"index":2, "c":5}]

d = defaultdict(dict)
for l in (l1, l2):
    for elem in l:
        d[elem['index']].update(elem)
l3 = d.values()


@app.route('/')
def index():
    context = {
        "planets": get_planets()['results'],
        "people": get_people()['results'],
        "both": get_planets()['results'] + get_people()['results'],
        "test": l3,
    }
    return render_template("index.html", **context, )


@app.route('/people_planet_details/<int:planet_id>')
def people_planet_details(person_id, planet_id):
    details = get_planet(planet_id)['name']
    return render_template("people.html", details=details)

if __name__ == "__main__":
    app.run(debug=True, port=8080, host='127.0.0.1')
