num=1
print("welcome to the game ")
print("please enter a number")
secret_number=25
attempt =10

while num<=10:
      attempt = attempt - 1
      print(f"attempts left:{attempt}")
      user_input=int(input("please enter the number "))
      if user_input == secret_number:
          print("your gess was right")
          user_input=True
          break
      else:
          if user_input > secret_number:
              print("the number is lower")
          else:
              print("the number is higher")

          num += 1

print("thankyou for playing the game")

