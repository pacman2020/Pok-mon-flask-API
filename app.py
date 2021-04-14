from flask import Flask, url_for, render_template, redirect, jsonify, json, request
from requests import get


app = Flask(__name__)

@app.route('/')
def home():
    search = request.args.get('search')
    
    if search:
        pokemonsJson = get('https://pokeapi.co/api/v2/pokemon/'+search)
        pokemon = json.loads(pokemonsJson.content)
        pokemons = []
        pokemons.append(
            {
                'id':  pokemon['id'],
                'name': pokemon['name']
            }
        )
        return render_template('home.html', pokemons=pokemons)
    
    pokemonsJson = get('https://pokeapi.co/api/v2/pokemon')
    all_pokemons = json.loads(pokemonsJson.content)
    pokemons = []
    id = 0
    for pokemon in all_pokemons['results']:
        id += 1
        pokemons.append(
            {
                'id': id,
                'name': pokemon['name']
            }
        )
    return render_template('home.html', pokemons=pokemons)

@app.route('/<name>')
def detail(name):
    pokemonsJson = get('https://pokeapi.co/api/v2/pokemon/'+name)
    pokemon_data = json.loads(pokemonsJson.content)
    pokemon = {
            'id':  pokemon_data['id'],
            'name': pokemon_data['name'],
            'type': pokemon_data['types'][0]['type']['name'],
            'weight': pokemon_data['weight'],
            'abilites1': pokemon_data['abilities'][0]['ability']['name'],
            'abilites2': pokemon_data['abilities'][1]['ability']['name'],
        }
    return render_template('detail.html', pokemon=pokemon)

if __name__ == '__main__':
    app.run(debug=True)