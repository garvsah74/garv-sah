#taking input from the user as "enter" for entering the game and 'q' for quitting the game .
import random
print ("welcome to the game of rolling a dice ")
choice= input("enter your choice 'enter' to play and 'q' to quit ")
if choice == 'q':
    print("thank you for playing the game")

elif choice == '':


    num= random.randint (1,6)
    print(f"the num is {num}")

else:
    print("invalid choice")
