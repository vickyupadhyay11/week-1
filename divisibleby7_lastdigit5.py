num = int(input("Enter a number: "))

if( num % 7 == 0 or num % 10 == 5):
    print(num, "is either divisible by 7 or its last digit is 5")
else:
    print(num, "does not satisfy the condition")
