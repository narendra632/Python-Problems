import random

i=0
no=0
lose=0
draw=0

print("\n")
print("Welcome to the SNAKE,WATER,GUN game. You have 10 Chances\n")


while(True):
    i=i+1

    list=["snake","water","gun"]
    n=random.choice(list)
    
    g=input("***Enter S for Snake, W for Water, G for Gun***\n:").lower()
   
    if g=="s" and n=="water":
       no=no+1
       print("Computer choice ",n)
       print("You won",no,"Time\n")
    elif g=="w" and n=="gun":
       no=no+1
       print("Computer choice ",n)
       print("You Won",no,"Times\n")
    elif g=="g" and n=="snake":
       no=no+1
       print("Computer choice ",n)
       print("You Won",no,"Times\n") 
    elif g==n[0].lower():
       draw=draw+1
       print("Computer choice ",n)
       print("Draw",draw,"Time\n")
    elif  g=="s" and n=="gun":
       lose=lose+1
       print("Computer choice ",n)
       print("You Lose",lose,"Times\n")
    elif  g=="w" and n=="snake":
       lose=lose+1
       print("Computer choice ",n)
       print("You Lose",lose,"Times\n")
    elif  g=="g" and n=="water":
       lose=lose+1
       print("Computer choice ",n)
       print("You Lose",lose,"Times\n")
    else:
       print("Wrong input")

    if i==10:
       print("\n***You Won",no,"Times***")
       print("***Draw",draw,"Times***")
       print("***Computer Won",lose,"Times***\n")
       break

if no > lose:
   print("You won computer lose")
elif no < lose:
   print("computer won you lose")
else:
   print("there is a draw")


   