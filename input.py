#write a program to input 3 numbers and print the minimum among them.
A=int(input("enter the first number:"))
B=int(input("enter the second number:"))
C=int(input("enter the third number:"))
if(A<B and A<C):
    print(" Ais the smallest number")
elif(B<C and B<A):
    print("B is the smallest number")
else:
    print("C is the smallest number")