print("Welcome to Python Poker. Creator's github is https://github.com/paulbadmanthereal")
import random

# Card values
card_values = {
    'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13
}

# Function to evaluate the player's hand
def evaluate_hand(hand):
    # Sort the hand by card values
    sorted_hand = sorted(hand, key=lambda x: card_values[x[0]])

    # Check for flush
    if len(set(card[1] for card in hand)) == 1:
        return "Flush"

    # Check for straight
    values = [card_values[card[0]] for card in sorted_hand]
    if len(set(values)) == 5 and (values[-1] - values[0] == 4 or values == [1, 10, 11, 12, 13]):
        return "Straight"

    # Check for four of a kind
    if any(values.count(value) == 4 for value in values):
        return "Four of a Kind"

    # Check for full house
    if any(values.count(value) == 3 for value in values) and any(values.count(value) == 2 for value in values):
        return "Full House"

    # Check for three of a kind
    if any(values.count(value) == 3 for value in values):
        return "Three of a Kind"

    # Check for two pairs
    if sum(1 for value in set(values) if values.count(value) == 2) == 2:
        return "Two Pairs"

    # Check for one pair
    if any(values.count(value) == 2 for value in values):
        return "One Pair"

    return "High Card"

# Function to make a bet
def make_bet(balance):
    while True:
        try:
            bet = int(input("Enter your bet amount: "))
            if bet <= 0:
                print("Bet amount must be a positive integer.")
            elif bet > balance:
                print("Insufficient funds. Please enter a lower bet.")
            else:
                return bet
        except ValueError:
            print("Invalid input. Please enter a valid bet amount.")

# Function for AI to make a decision
def ai_decision(hand, difficulty):
    evaluated_hand = evaluate_hand(hand)
    values = [card_values[card[0]] for card in hand]

    if difficulty >= 8 and evaluated_hand in ["Flush", "Straight", "Four of a Kind", "Full House"]:
        return "stand"
    elif difficulty >= 5 and evaluated_hand in ["Three of a Kind", "Two Pairs"]:
        return "stand"
    elif difficulty >= 3 and evaluated_hand == "One Pair" and max(values) >= 10:
        return "stand"
    else:
        return "hit"

# Function to play a game of poker
def play_poker(balance, difficulty):
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [(value, suit) for value in card_values for suit in suits]
    random.shuffle(deck)

    # Initialize player and AI hands
    player_hand = deck[:5]
    ai_hand = deck[5:10]

    # Place bet
    bet = make_bet(balance)
    balance -= bet

    print("Your initial hand:", player_hand)
    print("AI's initial hand: Hidden")

    # Player's turn
    discard_indices = input("Enter the indices of the cards you want to discard (comma-separated): ")
    discard_indices = [int(index) for index in discard_indices.split(",") if index.strip().isdigit()]

    new_cards = deck[10:10+len(discard_indices)]
    for index, card in zip(discard_indices, new_cards):
        player_hand[index] = card

    # AI's turn
    ai_action = ai_decision(ai_hand, difficulty)
    if ai_action == "hit":
        ai_discard_indices = random.sample(range(5), random.randint(1, 5))
        new_cards = deck[10+len(discard_indices):10+len(discard_indices)+len(ai_discard_indices)]
        for index, card in zip(ai_discard_indices, new_cards):
            ai_hand[index] = card

    # Print the final hands
    print("Your final hand:", player_hand)
    print("AI's final hand:", ai_hand)

    # Evaluate the hands
    player_result = evaluate_hand(player_hand)
    ai_result = evaluate_hand(ai_hand)

    print("Your result:", player_result)
    print("AI's result:", ai_result)

    # Determine the winner
    if hand_rank.index(player_result) > hand_rank.index(ai_result):
        print("You win!")
        balance += bet * 2
    elif hand_rank.index(player_result) < hand_rank.index(ai_result):
        print("AI wins!")
    else:
        print("It's a tie!")
        balance += bet

    return balance

# Hand rankings
hand_rank = [
    "High Card", "One Pair", "Two Pairs", "Three of a Kind",
    "Straight", "Flush", "Full House", "Four of a Kind"
]

# Start the game
balance = 1000
print("Your starting balance:", balance)

difficulty = int(input("Enter the difficulty level of the AI (1-10): "))

while True:
    balance = play_poker(balance, difficulty)
    print("Your current balance:", balance)
    play_again = input("Do you want to play again? (yes/no) ").lower()
    if play_again != 'yes' or balance == 0:
        print("https://github.com/paulbadmanthereal")
        print("Thanks for playing! Goodbye!")
        break