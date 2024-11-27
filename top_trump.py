import random

def create_player_card(player_name, available_names):
    """Let a player choose a card and enter its attributes."""
    print(f"\n{player_name}, choose your card from the following:")
    print(", ".join(available_names))

    while True:
        choice = input(f"\n{player_name}, enter the name of your card: ").capitalize()
        if choice in available_names:
            break
        print("Invalid choice. Please choose a valid card name.")
    
    print(f"\n{player_name} chose: {choice}")
    strength = int(input(f"Enter Strength (1-10) for {choice}: "))
    speed = int(input(f"Enter Speed (1-10) for {choice}: "))
    intelligence = int(input(f"Enter Intelligence (1-10) for {choice}: "))
    
    return {"name": choice, "Strength": strength, "Speed": speed, "Intelligence": intelligence}

def create_computer_card(available_names):
    """Let the computer choose a card and generate random attributes."""
    choice = random.choice(available_names)
    print(f"\nComputer chose: {choice}")
    attributes = {
        "Strength": random.randint(1, 10),
        "Speed": random.randint(1, 10),
        "Intelligence": random.randint(1, 10)
    }
    return {"name": choice, **attributes}

def display_card(card, owner):
    """Display a card's name and attributes."""
    print(f"\n{owner}'s card:")
    print(f"Name: {card['name']}")
    for key, value in card.items():
        if key != 'name':
            print(f"{key}: {value}")

def get_attribute_choice(player_name):
    """Ask the specified player to choose an attribute."""
    while True:
        choice = input(f"\n{player_name}, choose an attribute to compete (Strength, Speed, Intelligence): ").capitalize()
        if choice in ["Strength", "Speed", "Intelligence"]:
            return choice
        print("Invalid choice. Please choose a valid attribute.")

def determine_winner(player_cards, attribute):
    """Determine the winner based on the chosen attribute."""
    values = {player: card[attribute] for player, card in player_cards.items()}
    max_value = max(values.values())
    winners = [player for player, value in values.items() if value == max_value]

    for player, value in values.items():
        print(f"{player}'s {attribute}: {value}")
    
    if len(winners) == 1:
        return winners[0]  # Single winner
    else:
        return None  # It's a draw

def play_game():
    """Main function to play the game."""
    print("Welcome to Top Trumps with 3 players!")
    available_names = ["Phoenix", "Griffin", "Cyclops", "Minotaur", "Centaur"]
    winner = "Player 1"  # Default first round starter

    while True:
        print("\nNew Round!")
        print("\nCards to choose from:", ", ".join(available_names))

        player1_card = create_player_card("Player 1", available_names)
        player2_card = create_player_card("Player 2", available_names)
        computer_card = create_computer_card(available_names)

        player_cards = {
            "Player 1": player1_card,
            "Player 2": player2_card,
            "Computer": computer_card
        }

        # Display all cards
        for player, card in player_cards.items():
            display_card(card, player)

        # Current winner chooses an attribute
        chosen_attribute = get_attribute_choice(winner)

        # Determine and print the winner
        round_winner = determine_winner(player_cards, chosen_attribute)
        if round_winner:
            print(f"\n{round_winner} wins this round!")
            winner = round_winner  # Update the winner for the next round
        else:
            print("\nIt's a draw! Player 1 will start the next round.")

        # Display all cards at the end of the round
        print("\nFinal Cards of this Round:")
        for player, card in player_cards.items():
            display_card(card, player)

        # Ask to play again or stop
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Start the game
play_game()
