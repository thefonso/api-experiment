import random
from flask import Flask, render_template
from starwars import (get_films, get_planet, get_planets, get_ship, get_people)
from collections import defaultdict

app = Flask(__name__)

list2 = get_planets()['results']
list1 = get_people()['results']

# d = defaultdict(dict)
# for l in (l1, l2):
#     for elem in l:
#             d[elem['name']].update(elem)
# l3 = d.values()

list3 = [{'name': x['name'], 'persons': [y['name'] for y in list1 if y['homeworld'] == x['url']]} for x in list2]

list3 = [x for x in list3 if x['persons']]

# print(list3)


@app.route('/')
def index():
    context = {
        "planets": get_planets()['results'],
        "people": get_people()['results'],
        "both": get_planets()['results'] + get_people()['results'],
        "test": list3,
    }
    return render_template("index.html", **context, )


@app.route('/people_planet_details/<int:planet_id>')
def people_planet_details(person_id, planet_id):
    details = get_planet(planet_id)['name']
    return render_template("people.html", details=details)

if __name__ == "__main__":
    app.run(debug=True, port=8080, host='127.0.0.1')
