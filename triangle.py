#you are given 3 integer angles of a triangle .tell whether the triangle is valid or not.
A=int(input("enter the first angle: "))
B=int(input("enter the second angle:"))
C=int(input("enter the third angle:"))
TOA=A+B+C
if TOA==2180:
    print("the triangle is valid")
else:
    print("the triangle is not valid")