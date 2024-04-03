# find a grade based on the input
# A = 90 to 100

# 3 steps to figure out
# step1 : inputs
# step2 : Logic
# step3 : result

scale = int(input("Enter the number you got:"))
if scale <= 100 and scale >= 90:
    print("Grade A")
elif scale <= 89 and scale >= 80:
    print("Grade B")
elif scale <= 79 and scale >= 70:
    print("Grade C")
elif scale <= 69 and scale >= 60:
    print("Grade D")
elif scale <= 59 and scale >=0:
    print("Grade F")
else:
    print("Invalid Input")
