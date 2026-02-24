import math
num=int(input("enter the number"))
# calculating the sqt
if num>=0:
    sqrt_of_num = math.sqrt(num)
    print(f"the square root of {num} is {sqrt_of_num}")
else:
    print(f"the {num} is invalid.CAN'T FIND SQRT OF THE NUMBER")
# calculating the (log base e)
if num>0:
    log_e=math.log(num)
    print(f"the log of {num} is {log_e}")
else:
    print(f"THE {num} IS INVALID")
#calculating the sin
sin_num=math.sin(num)
print(f"the sin of {num} is {sin_num}")
