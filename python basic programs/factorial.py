#factorial of number
num= int(input("enter any number"))
fact =1
if (num == 0):
    print("factorial don't exist")
else:
    for i in range(num,1,-1):
        fact = fact*i
print("factrorial of num is :",fact)
 
