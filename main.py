from logo import game_start, vs_logo
import random
score = 0
print(game_start) # Display the game start logo
from data import data 
celeb_A = random.choice(data)
celeb_A_folowers = celeb_A['number_of_followers_on_instagram']
print (f"Compare {celeb_A['name']}, a {celeb_A['profession']}, aged {celeb_A['age']}.")
print(vs_logo)
celeb_B = random.choice(data)
celeb_B_folowers = celeb_B['number_of_followers_on_instagram']
if celeb_B == celeb_A:
    celeb_B = random.choice(data)
    celeb_B_folowers = celeb_B['number_of_followers_on_instagram']
print(f"Against {celeb_B['name']}, a {celeb_B['profession']}, aged {celeb_B['age']}.")
guess =input("Who has more followers on Instagram? Type 'A' or 'B': ").lower()

def compare(guess, celeb_A, celeb_B):
    if guess == 'a':
        return celeb_A['number_of_followers_on_instagram'] > celeb_B['number_of_followers_on_instagram']
    elif guess == 'b':
        return celeb_B['number_of_followers_on_instagram'] > celeb_A['number_of_followers_on_instagram']
    else:
        return None  
             
game = True    
while game:
    if compare(guess, celeb_A, celeb_B):
        score += 1
        print(f"You're right! Current score: {score}.")
        celeb_A = celeb_B
        celeb_A_folowers = celeb_A['number_of_followers_on_instagram']
        print (f"Compare {celeb_A['name']}, a {celeb_A['profession']}, aged {celeb_A['age']}.")
        print(vs_logo)
        celeb_B = random.choice(data)
        celeb_B_folowers = celeb_B['number_of_followers_on_instagram']
        if celeb_B == celeb_A:
            celeb_B = random.choice(data)
            celeb_B_folowers = celeb_B['number_of_followers_on_instagram']
        print(f"Against {celeb_B['name']}, a {celeb_B['profession']}, aged {celeb_B['age']}.")
        guess = input("Who has more followers on Instagram? Type 'A' or 'B': ").lower()
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game = False