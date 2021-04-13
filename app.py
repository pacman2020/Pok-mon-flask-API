from flask import Flask, url_for, render_template, redirect, jsonify, json
from requests import get


app = Flask(__name__)

@app.route('/')
def home():
    pokemonsJson = get('https://pokeapi.co/api/v2/pokemon')
    all_pokemons = json.loads(pokemonsJson.content)
    pokemons = []
    id = 0
    for pokemon in all_pokemons['results']:
        id += 1
        pokemons.append(
            {
                'id': id,
                'name': pokemon['name'],
                'url': pokemon['url']
            }
        )
    return render_template('home.html', pokemons=pokemons)

if __name__ == '__main__':
    app.run(debug=True)