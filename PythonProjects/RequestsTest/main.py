import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'd8d520a37c016b0b04d39a6ec9cce6b0'
HEADER = {'Content-Type' : 'application/json' , 'trainer_token' : TOKEN}

body_pokemons = {
    "name": "Пикачу",
    "photo_id": 1 
}

body_change_name = {
    "pokemon_id": "274285",
    "name": "Пикачулли",
    "photo_id": 1
}

body_take_pokemon = {
    "pokemon_id": "274285"
}



'''response_pokemons = requests.post(url = f'{URL}/pokemons' , headers = HEADER , json = body_pokemons)
print(response_pokemons.text)'''

'''response_change_name = requests.put(url = f'{URL}/pokemons' , headers = HEADER , json = body_change_name)
print(response_change_name.text)'''

response_take_pokemon = requests.post(url = f'{URL}/trainers/add_pokeball' , headers = HEADER , json = body_take_pokemon)
print(response_take_pokemon.text)