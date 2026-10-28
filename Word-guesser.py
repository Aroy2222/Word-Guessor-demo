import random
health = 3
print("welcome to the word guessing game!")

def hint(): 
    if bot_choice in fruits:
        print("Hint: It's a type of fruit.")
    elif bot_choice in vehicles:
        print("Hint: It's a type of vehicle.")
    elif bot_choice in vegetables:
        print("Hint: It's a type of vegetable.")
    elif bot_choice in fastfoods:
        print("Hint: It's a type of fast food.")
    elif bot_choice in seafoods:
        print("Hint: It's a type of seafood.")
    elif bot_choice in sosses:
        print("Hint: It's a type of sauce.")

fruits = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon", "mango", "nectarine"]
vehicles = ["car", "bike", "bus", "train", "plane", "boat", "scooter", "truck", "van", "submarine"]
vegetables = ["carrot", "broccoli", "spinach", "pepper", "onion", "potato", "tomato", "cucumber", "lettuce", "zucchini"]
fastfoods = ["burger", "pizza", "fries", "hotdog", "taco", "sandwich", "nuggets", "pasta", "sushi", "icecream"]
seafoods = ["salmon", "shrimp", "crab", "lobster", "tuna", "squid", "oyster", "clam", "mussel", "octopus"]
sosses = ["ketchup", "mustard", "mayonnaise", "barbecue", "ranch", "hot sauce", "soy sauce", "teriyaki", "pesto", "salsa"]
    
all_words = fruits + vehicles + vegetables + fastfoods + seafoods + sosses
bot_choice = random.choice(all_words)
while health > 0:   
    input_word = input("Guess the word: ").lower()

    if input_word == bot_choice:
            print("Congratulations! You guessed the word correctly the word was: " + bot_choice)
            print("play again? (yes/no)")
            play_again = input().lower()
            if play_again == "yes":
                health = 3
                bot_choice = random.choice(all_words)
                continue 
            else:
                break
    else:   
         health -= 1
         print(f"Wrong guess! You have {health} health left.")
         hint()

    if health <= 0:
        print("Game over! You've run out of health.")
    
