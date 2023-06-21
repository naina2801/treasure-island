print("welcome to Treasure Island")
print("Your mission is to find the treasure")
choice1= input('you\'re at a crossroad, where do you want to go ? Type "left" or "Right" : ').lower()
if choice1 == 'left':
    choice2= input('you\'ve come to lake. there is an island in the middle of the lake. Type "wait" to wait for a boat.Type "swim" to swim to across : ').lower()
    if choice2 == 'wait':
        choice3 = input('which door do you choose.Type "Red" or "Blue" or "Black : "').lower()
        if choice3 == "blue":
            print("You found the treasure ! You win!")
        elif choice3 == "red":
            print("it's a room full of fire,Game over")
        elif choice3 == "black":
            print("you enter a room of beasts,Game over")
        else:
            print("You chose a door that doesn't exist, Game Over")
    else:
        print("you got attacked by an angry trout,Game over")
else:
    print("you fell into a hole.Game Over.")


