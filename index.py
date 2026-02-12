import random
print("="*50)
print("       🎲 Welcome to Dice Rolling Game 🎲")
print("="*50)

while True:
    print('''\npress 1 for rolling dice:-
press 2 for exit:-''')

    choice=int(input("enter your choice:-"))
    if choice==1:
        dice=random.randint(1,6)
        print("your rolling number:-",dice)

        if dice == 6:
            print(" 6 now can you role aagin :-")
        else:
            print("thanks for rolling dice:-")

    elif choice==2:
        print("exiting:-","\n")
        print("="*50)
        break
  
    else:
        print("invalid number try again:-")
        print("="*50)
    