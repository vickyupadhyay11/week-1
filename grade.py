#Accept the percentage from the user and display the grade according to criteria.
percentage=int(input("enter the percentage you got :"))
if(percentage>=90 and percentage<100):
    print("O grade")
elif(percentage>=80 and percentage<90):
    print("A grade")
elif(percentage>=70 and percentage<80):
    print("A grade")
elif(percentage>=60 and percentage<70):
    print("B grade")
elif(percentage>=50 and percentage<60):
    print("C grade")
elif(percentage>=40 and percentage<50):
    print("pass")
elif(percentage<40):
    print("fail")