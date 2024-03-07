fruits = ["apple","banana","mango","orange","pineapple","kiwi","grapes","dragonfruit","strawberry"]
dry = ["kaju","almond","pista","kishmish"]

def print_length(list): #for length of any list
    print(len(list))

print_length(dry)

def print_singleline(list):   # function fo print multiple lists in single line
    for item in list:
        print(item,end=" ")
print_singleline(fruits) 
print_singleline(dry)  

def fact_num(n):   #factorial of a number
    num = 1
    for i in range(1,n+1):
        num *= i
    print(num)
  
fact_num(5)




