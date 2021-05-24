import logo
import data
import random

print(logo.logo)

def generate_data_a():
        rand_person_a = random.choice(data.data)
        return rand_person_a

def generate_data_b():
    rand_person_b = random.choice(data.data)
    return rand_person_b

def check_player_guess():
    if player_guess < against:
        return 0
    elif player_guess > against:
        return 1

game_start = True
while game_start:
    score = 0

    game_over = False
    while not game_over:

        dictionary_a = generate_data_a()
        dictionary_b = generate_data_b()
        #print(dictionary_a)
        #print(dictionary_b)

        #check data is not the same
        proceed = False
        while not proceed:
            if dictionary_a['name'] == dictionary_b['name']:
                dictionary_b = generate_data_b()
            else:
                proceed = True

        follower_count_a = dictionary_a['follower_count']
        follower_count_b = dictionary_b['follower_count']

        #print(follower_count_a)
        #print(follower_count_b)



        proceed = False
        while not proceed:
            guess = input(f"Which Instagram account has more followers:\n{dictionary_a['name']} - description: {dictionary_a['description']} from {dictionary_a['country']}\nOR\n{dictionary_b['name']} - description: {dictionary_b['description']} from {dictionary_b['country']}\nAnswer: ").title()
            if guess == dictionary_a['name']:
                player_guess = dictionary_a['follower_count']
                against = dictionary_b['follower_count']
                proceed = True
            elif guess == dictionary_b['name']:
                player_guess = dictionary_b['follower_count']
                against = dictionary_a['follower_count']
                proceed = True
            else:
                print(f"Sorry, that name was not recognised. Please enter either {dictionary_a['name']} or {dictionary_b['name']}")
                proceed = False

        if check_player_guess() == 0:
            print(f"That was incorrect")
            game_over = True
        elif check_player_guess() == 1:
            print(f"You were correct {dictionary_a['name']} has {dictionary_a['follower_count']} million followers, compared with {dictionary_b['name']} who has {dictionary_b['follower_count']} million followers")
            score += 1
            game_over = False

    print(f"Your final score was {score}")
    game_restart = input("Would you like to play again? Y/N: ").lower()
    if game_restart == "y":
        game_start = True
    else:
        game_start = False
print("Thank you for playing, goodbye")






