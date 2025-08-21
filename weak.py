# Read number from user
day_num = int(input("Enter a number (1-7): "))

# Map number to day
if day_num == 1:
    print("Sunday")
elif day_num == 2:
    print("Monday")
elif day_num == 3:
    print("Tuesday")
elif day_num == 4:
    print("Wednesday")
elif day_num == 5:
    print("Thursday")
elif day_num == 6:
    print("Friday")
elif day_num == 7:
    print("Saturday")
else:
    print("Invalid input! Please enter a number between 1 and 7.")
