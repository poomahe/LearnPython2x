#Factorial
import math

num = int(input("Enter the number:"))
factorial = 1
if num < 0:
    print(f"Entered {num} is negative or not applicable")
elif num == 0:
    print(f"The factorial of zero is 1")
else:
    for i in range(1,num+1):
        factorial = factorial * i
print(factorial)