import random

random_int = random.randint(1,10)
inp = input ("Guess a number between 1 and 10: ")
imp = int(inp)

while random_int != imp:
    print ('incorrect')
    if imp > random_int:
        print ('A little lower!')
    if imp < random_int:
        print ('A little higher!')
    inp = input ("Guess a number between 1 and 10: ")
    imp = int(inp)

print ('correct!')