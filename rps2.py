import random

choices = ["r", "p", "s"]
p1Wins = 0
p2Wins = 0
on = True
gameCount = 0

while on:
    p1 = input("Rock, Paper or Scissors? ")    
    p2 = random.choice(choices)
    
    print(p1)
    print(p2)
    
    if p1 == "r" and p2 == "s" or p1 == "p" and p2 == "r" or p1 == "s" and p2 == "p":
        print("p1 Wins")
        p1Wins += 1
    elif p1 == p2:
        print("Draw")
    
    else:
        print("p2 Wins")
        p2Wins += 1
    
    print("p1 wins = " + str(p1Wins) + "\np2 wins = " + str(p2Wins))
    if p1Wins == 5 or p2Wins == 5:
        on = False

