from flask import Flask, url_for, render_template, redirect, jsonify, json, request
from requests import get

# ?limit=100&offset=200

app = Flask(__name__)

@app.route('/')
def home():
    limit = 3
    offset = 6
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
    
    url = 'https://pokeapi.co/api/v2/pokemon?limit={}&offset={}'.format(limit, offset)
    
    pokemonsJson = get('https://pokeapi.co/api/v2/pokemon?limit=3&offset=6')
    all_pokemons = json.loads(pokemonsJson.content)
    # print('--->', all_pokemons['results'])
    pokemons = []
    id = 0
    for pokemon in all_pokemons['results']:
        
        # extracting pokemon id by URL
        id_p = pokemon['url']
        id = id_p[-2]

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