#Leap Year or not

year = int(input("Enter the year you want to check:"))
if year%4 == 0:
    print(f"Entered {year} is leap year")
else:
    print(f"Entered {year} is not leap year")
