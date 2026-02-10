import random

random_int = random.randint(1,10)
inp = input ("Guess a number between 1 and 10: ")
imp = int(inp)
user_list = []

while random_int != imp:
    user_list.append(imp)
    print('you have already guessed: ', user_list)
    if imp > random_int:
        print ('A little lower!')
    if imp < random_int:
        print ('A little higher!')
    inp = input ("Guess a number between 1 and 10: ")
    imp = int(inp)

print ('correct!')
print ('your guesses: ', user_list)