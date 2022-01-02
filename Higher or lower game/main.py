from game_data import data
import random

print(data[0]['name'])

points_score = 0

def get_card(card_letter, card_position):
    print(f"{card_letter}: {data[card_position]['name']}, a {data[card_position]['description']} from {data[card_position]['country']}")

def get_score():
    print(f"Points score: {points_score}\n")

while True:
    first_card = random.randint(0, len(data) - 1)
    second_card = random.randint(0, len(data) - 1)
    
    get_card('A', first_card)
    get_card('B', second_card)
    answer = input("Which one do you think has more followers? 'A' or 'B'?\n")
    
    if data[first_card]['follower_count'] > data[second_card]['follower_count']:
        if answer == 'A':
            print("You're right!\n")
            points_score += 1
            get_score()
        else:
            print("You're wrong! Game over!\n")
            break
    else:
        if answer == 'B':
            print("You're right!\n")
            points_score += 1
            get_score()
        else:
            print("You're wrong! Game over!\n")
            break
    
get_score()
    
