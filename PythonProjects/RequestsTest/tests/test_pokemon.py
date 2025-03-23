import requests
import pytest 

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'd8d520a37c016b0b04d39a6ec9cce6b0'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = 24031
def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200