#using single line conditonal statements
food=input(" do you want to eat")
eat ="yes i like it " if food=="cake" else "no i dont like it "
print(eat )
#using claver conditions in following code
age =int(input("my age is "))
vote=("yes i can vote ","no i can vote")[age<=18]
print(vote)
#good practice
#simple intrest
p=int(input("principal"))
r=int(input("rate "))
t=int(input("time"))
si=(p*r*t)/100
print("simple intrest is =",si)