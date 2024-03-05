#question 1:
#even odd

num = int(input("enter any number"))
if(num % 2 == 0):
    print("even")
else:
    print("odd")

# question 2:
#greatest of three
a = int(input("enter value of a \n"))
b = int(input("enter value of b \n"))
c = int(input("enter value of c \n"))
if(a > b & b > c):
    print("a is greater")
elif(b > a & a > c):
    print("b is greater")
else:
    print("c is greater")

# question 3:
#check number is multiple of 7 or not
que = int (input("enter any number"))
if(que % 7 == 0):
    print("number is multiple of 7")
else:
    print("wrong info")
