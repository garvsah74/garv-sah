balance = 0.0

def check_balance():
    print("===================")
    print(f"your bank balance is {balance}")
    print("===================")

def deposit(amount):
    global balance
    if  amount>0:
        balance+=amount
        print(f"amount deposited is {amount}")
    else:

     print("===================")
     print(f"invalid amount ")
     print("===================")

def withdraw(amount):
    global balance
    if amount<=0:
        print(" error")
    elif balance<amount:
      print("insufficient balance ")

    else: balance-=amount
    print("===================")
    print(f"amount withdrawn is {amount}")
    print("===================")

if  __name__ == "__main__":
    print("===================")
    print("welcome to the coding bank")
    print("===================")

    while True:
         print("1:check balance")
         print("2: deposit")
         print("3:withdraw")
         print("4:quit")

         choice=input("please enter your choice ('1-4')")


         if choice=="1":
           check_balance()
         elif choice=="2":
          amt =int(input("enter the amount to be deposited"))
          deposit(amt)
          print(f"amount{amt} deposited is successfully")

         elif choice =="3":
          amt=(float(input("enter the amount to be withdrawn")))
          withdraw(amt)
          print(f"amount{amt} withdrawn  successfully")

         elif choice=="4":
             print("###############")
             print("quitting the program")
             print("###############")

             break
         else:
             print("invalid choice")


    print("thankyou for choosing our bank")





