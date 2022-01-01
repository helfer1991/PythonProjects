############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print("Welcome to the 100 Days of Python version of BlackJack")

answer = ''
player_hand = []
computer_hand = []
limit_blackjack = 21

def update_hand(hand):
    hand.append(cards[random.randint(0, len(cards) - 1)])

def calculate_points(hand):
    return sum(hand)

while answer != 'n':
    answer = input("Do you want to play a game of Blackjack? 'y' or 'n': \n")

    if answer == 'y':
        player_score = 0
        computer_score = 0
        take_another_card = ''
        update_hand(player_hand)
        update_hand(computer_hand)

        while take_another_card != 'n':
            player_score = calculate_points(player_hand)
            computer_score = calculate_points(computer_hand)
            
            if player_score > limit_blackjack or computer_score > limit_blackjack:
                print(f"Your final hand: {player_hand}, your final score: {player_score}\n")
                print(f"Computer final hand: {computer_hand}, computer final score: {computer_score}\n")
                take_another_card = 'n'
                player_hand.clear()
                computer_hand.clear()

                if player_score < computer_score and player_score < limit_blackjack:
                    print("You won!\n")
                else:
                    print("Computer won!\n")
                    
            else:
                print(f"Your cards: {player_hand}\nYour current score: {player_score}\nComputer's first card: {computer_hand[0]}\n")
                take_another_card = input ("Do you want to take another card or pass? 'y' or 'n': \n")
                update_hand(player_hand)
                update_hand(computer_hand)