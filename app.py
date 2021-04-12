from flask import Flask, url_for, render_template, redirect, jsonify, json
from requests import get


app = Flask(__name__)

@app.route('/')
def home():
    pokemons = get('https://pokeapi.co/api/v2/pokemon')
    all_pokemons = json.loads(pokemons.content)
    data = []
    id = 0
    for pokemon in all_pokemons['results']:
        id += 1
        data.append(
            {
                'id': id,
                'name': pokemon['name'],
                'url': pokemon['url']
            }
        )
    return render_template('home.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)