import random
import requests


def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_number}/'
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
    }


def play_round(player_score, opponent_score):
    my_pokemon = random_pokemon()
    print('\nYou were given {}'.format(my_pokemon['name']))
    stat_choice = input('Which stat do you want to use? (id, height, weight) ')

    opponent_pokemon = random_pokemon()
    print('The opponent chose {}'.format(opponent_pokemon['name']))

    my_stat = my_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]

    print(f'Your {stat_choice}: {my_stat}')
    print(f'Opponent {stat_choice}: {opponent_stat}')

    if my_stat > opponent_stat:
        print('You Win this round!')
        return player_score + 1, opponent_score
    elif my_stat < opponent_stat:
        print('You Lose this round!')
        return player_score, opponent_score + 1
    else:
        print('This round is a Draw!')
        return player_score, opponent_score


def run():
    player_score = 0
    opponent_score = 0

    print("Welcome to the Pokemon Stats Battle!")
    rounds = int(input("How many rounds would you like to play? "))

    for round_num in range(rounds):
        print(f"\n=== Round {round_num + 1} ===")
        print(f"Current Score - You: {player_score}, Opponent: {opponent_score}")

        player_score, opponent_score = play_round(player_score, opponent_score)

    print("\n=== Final Results ===")
    print(f"Your final score: {player_score}")
    print(f"Opponent final score: {opponent_score}")

    if player_score > opponent_score:
        print("Congratulations! You're the winner! 🏆")
    elif player_score < opponent_score:
        print("Game Over! You lost! Better luck next time! 😢")
    else:
        print("It's a tie! 🤝")

    play_again = input("\nWould you like to play again? (yes/no) ").lower()
    if play_again.startswith('y'):
        run()


if __name__ == '__main__':
    run()