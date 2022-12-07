import requests
data_pakemon = {
 "name": "Makatao"
}
response = requests.post("https://pokemonbattle.me:5000//pokemons", 
headers={"trainer_token": "09eed286d87db1c813c30ed9cb7d201a"},
json=data_pakemon)
print(response.json())


import requests
data_pakemon = {
"pokemon_id": "1434",
"name": "Dopelgun"
}
response = requests.put("https://pokemonbattle.me:5000//pokemons", 
headers={"trainer_token": "09eed286d87db1c813c30ed9cb7d201a"},
json=data_pakemon)
print(response.json())


import requests

data_pakemon = {
"pokemon_id": "1434"
}
response = requests.post("https://pokemonbattle.me:5000//trainers/addPokebol", 
headers={"trainer_token": "09eed286d87db1c813c30ed9cb7d201a"},
json=data_pakemon)
print(response.json())
