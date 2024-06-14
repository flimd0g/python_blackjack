cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

import art
import random
import sys


def first_deal():
    user_total = 0
    # Assign two random cards to user. Print both as well as total
    random_cards = random.choices(cards, k=2)
    user_cards = random_cards
    for card in user_cards:
        user_total += card
    print("Your cards are " + str(user_cards) + " Total: " + str(user_total))
    # Assign two random cards to CPU. Print only one.
    cpu_total = 0
    random_cards = random.choices(cards, k=2)
    cpu_cards = random_cards
    for card in cpu_cards:
        cpu_total += card
    print("CPU's first card is: " + str(cpu_cards[0]))
    return cpu_cards, user_cards, user_total, cpu_total


# Hit me function. Adds another card.
def hit_me(user_cards, user_total):
    new_card = random.choice(cards)
    user_cards.append(new_card)
    user_total += new_card
    return user_cards, user_total


# cpu turn function. When the user decide's they're close enough to 21.
def cpu_turn(cpu_cards, cpu_total):
    if cpu_total < 17:
        new_card = random.choice(cards)
        cpu_cards.append(new_card)
        cpu_total += new_card
        return cpu_cards, cpu_total
    else:
        return cpu_cards, cpu_total


# Starting screen
print(art.logo)
restart_game = False
while not restart_game:
    game_start = input("Start a new game?: 'Y', 'N': ").lower()
    if game_start == "y":
        print("Starting game...")
        cpu_cards, user_cards, user_total, cpu_total = first_deal()
    elif game_start == "n":
        print("Naff off then!")
        sys.exit()

    gamestate = True
    while gamestate:
        if user_total == 21:
            cpu_cards, cpu_total = cpu_turn(cpu_cards, cpu_total)
            print(f"CPU cards: {cpu_cards} / Total: {cpu_total}")
            print("Blackjack! You win!")
            gamestate = False

        elif user_total > 21:
            cpu_cards, cpu_total = cpu_turn(cpu_cards, cpu_total)
            print("Bust! You lose.")
            gamestate = False

        else:
            user_move = input("Do you want another card? 'Y', 'N': ").lower()

            if user_move == "y":
                user_cards, user_total = hit_me(user_cards, user_total)
                print(f"User cards: {user_cards} Total: {user_total}")

            elif user_move == "n":
                cpu_cards, cpu_total = cpu_turn(cpu_cards, cpu_total)
                print(f"User cards: {user_cards} Total: {user_total}")
                print(f"CPU cards: {cpu_cards} / Total: {cpu_total}")
                if cpu_total > 21:
                    print("CPU busts, you win!")
                    gamestate = False
                elif cpu_total < user_total:
                    print("You win!")
                    gamestate = False
                elif cpu_total > user_total:
                    print("CPU wins.")
                    gamestate = False
                else:
                    print("It's a tie")
                    gamestate = False








