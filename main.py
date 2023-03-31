import random
from art import logo
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_card = []
computer_cards = []

def get_user_random_card(number_of_cards):
    for number in range(0,number_of_cards):
        user_random = random.choice(cards)
        if cards.index(user_random) == 0:
            ace_value = int(input("ace value '11' or '1' ?"))
            if ace_value == "1":
                user_random = 1
            
        user_card.append(user_random)

    return f"user card list = {user_card}"
    
def get_computer_random_card(number_of_cards):
    for number in range(0,number_of_cards):
        computer_random = random.choice(cards)
        computer_cards.append(computer_random)
    return f"computer card list = {computer_cards}"

def sum(list):
    sum = 0
    for card in list:
        sum += card
    return sum    

user = get_user_random_card(2)
print(user)
computer = get_computer_random_card(1)
print(computer)

want_card = True
while want_card:
    user_card_sum = sum(user_card)
    if user_card_sum >= 21:
        want_card = False
    else:   
        want_another_card = input("Do you want another card?'y' or 'n'? ")

        if user_card_sum >=21:
            want_card = False
        if want_another_card =="y":
            print(get_user_random_card(1))
        else:
            want_card = False

print(get_computer_random_card(1))



user_card_sum = sum(user_card)
print(f"users card sum is = {user_card_sum}")

comp_cards_sum = sum(computer_cards)
print(f"computer cards sum is = {comp_cards_sum}")



while comp_cards_sum < 17:
    print("computer card sum is less then 17")
    print(get_computer_random_card(1))
    comp_cards_sum = sum(computer_cards)
    print(f"the final computer cards sum is = {comp_cards_sum}")



if user_card_sum > 21 and comp_cards_sum > 21:
    print("draw")
elif user_card_sum > 21:
    print("you lost")
elif comp_cards_sum > 21:
    print("you win")
elif user_card_sum > comp_cards_sum:
    print("you win")
elif user_card_sum == comp_cards_sum:
    print("draw")
else:
    print("computer won")