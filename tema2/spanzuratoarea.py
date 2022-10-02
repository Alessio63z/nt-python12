import random
cities_list = ['ORAVITA', 'TIMISOARA', 'BUCURESTI', 'ORADEA', 'CLUJ', 'RESITA', 'TARGOVISTE', 'IASI', 'SIBIU', 'ARAD']
city = random.choice(cities_list)
mistakes = 3
guesses = []
made = False
while not made:
    for text in city:
        if text.lower() in guesses:
            print(text, end=' ')
        else:
            print("_", end=" ")
    print("")
    guess = input(f"Errors left {mistakes}, next guess > ")
    guesses.append(guess.lower())
    if guess.lower() not in city.lower():
        mistakes -= 1
        if mistakes == 0:
            break

    made = True
    for text in city:
        if text.lower() not in guesses:
            made = False
if made:
    print(f'Congratulations you won! The word is:  {city}!')

else:
    print(f'Unfortunately you lost! The word was: {city}!')