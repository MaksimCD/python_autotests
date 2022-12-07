import pytest
import requests

def test_status_code():
    url = "https://pokemonbattle.me:5000/trainers"
    response = requests.get(url)
    assert response.status_code == 200

def test_piece_body():
    response = requests.get("https://pokemonbattle.me:5000/trainers", params= {"trainer_id":"1226"}) 
    response = response.json()
    assert response["trainer_name"] == "Gaz"  
