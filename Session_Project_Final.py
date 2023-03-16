import random
import requests
player_wins = 0

def random_pokemon():
    opponent_pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(opponent_pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'order': pokemon['order'],
        'base_experience': pokemon['base_experience'],
    }


for wins in range(3):

    player_pokemon_number = input("Choose a number between 1 and 151 to pick a pokemon: ")
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(player_pokemon_number)
    response = requests.get(url)
    player_pokemon_number = response.json()
    print("Name: " + player_pokemon_number['name'])
    print("ID: " + str(player_pokemon_number['id']))
    print("Height: " + str(player_pokemon_number['height']))
    print("Weight: " + str(player_pokemon_number['weight']))
    print("Order: " + str(player_pokemon_number['order']))
    print("Base_experience: " + str(player_pokemon_number['base_experience']))

    poke_stat = {
        'name': player_pokemon_number['name'],
        'id': player_pokemon_number['id'],
        'height': player_pokemon_number['height'],
        'weight': player_pokemon_number['weight'],
        'order': player_pokemon_number['order'],
        'base_experience': player_pokemon_number['base_experience']
    }

    choose_stat: str = input('Select a stat (lowercase): "id/height/weight/order/base_experience"')


    opponent_pokemon_number = random_pokemon()

    print('The opponent chose {}'.format(opponent_pokemon_number['name']))

    print("Name: " + opponent_pokemon_number['name'])
    print("ID: " + str(opponent_pokemon_number['id']))
    print("Height: " + str(opponent_pokemon_number['height']))
    print("Weight: " + str(opponent_pokemon_number['weight']))
    print("Order: " + str(opponent_pokemon_number['order']))
    print("Base_experience: " + str(opponent_pokemon_number['base_experience']))

    player_stat = player_pokemon_number[choose_stat]
    opponent_stat = opponent_pokemon_number[choose_stat]

    if player_stat > opponent_stat:
        print('You Win!')

        player_wins = player_wins + 1

    elif player_stat < opponent_stat:
        print('You Lose!')

    else:
        print('Draw!')

if player_wins == 2:
    print('Final outcome: you win 2/3!')
else:
    print('Final outcome: you lose, try again')