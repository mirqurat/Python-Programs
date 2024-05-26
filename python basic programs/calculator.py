first = input("enter first number \n ")
operator = input("enter operator(+,-,*,/,%,//,**) \n")
second = input("enter seconde number \n ")
first =int(first)
second = int(second)
if operator =="+":
    print("sum of ",first ,"and" ,second ," number is = ",first+second)
elif operator =="-":
     print("subraction  of ",first ,"and" ,second ," number is = ",first-second)
elif operator =="*":
      print(" multiplication of ",first ,"and" ,second ," number is = ",first*second)
elif operator =="/":
       print("division  of ",first ,"and" ,second ," numberis = ",first/second)
elif operator =="%":
     print("modules of ",first ,"and" ,second ,"is = ",first%second)
elif operator =="//":
     print("division2 of ",first ,"and" ,second ,"is = ",first//second)
elif operator =="**":
     print("power of ",first ,"and" ,second ,"is = ",first**second)
else:
    print("operator not found")