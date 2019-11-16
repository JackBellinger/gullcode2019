import random

def matches(ar1, ar2):
    for i in range(4):
        if (ar1[i] != ar2[i]):
            return False

    return True

def to_array(x):
    array = [0, 0, 0, 0]
    for i in range(4):
        array[3-i] = x%10
        x = int(x/10)
    return array

Heff = []

Heff.append(int(random.random()*10))
for i in [0,1,2]:
    new_int = int(random.random()*10)
    while(new_int in Heff):
        new_int = int(random.random()*10)
    Heff.append(new_int)
#print("Debug")
#print(Heff)
guess = int(input())

Heff_guess = to_array(guess)
#print(Heff_guess)
while not matches(Heff, Heff_guess):
    bulls = 0
    cows = 0
    for i in range(4):
        if (Heff[i] == Heff_guess[i]):
            bulls += 1
        elif(Heff_guess[i] in Heff):
            cows += 1
    print ("Bulls: {}\nCows: {}".format(bulls, cows))
    guess = int(input())
    Heff_guess = to_array(guess)

print ("Guessed it")
