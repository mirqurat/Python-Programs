x = lambda num :num*2
print(x(10))
nl =[2,5,3,6,7,8,11,15,4]
result = list(filter(lambda x:(x % 2 == 0),nl))
print(result)
result = list(filter(lambda x:(x%2),nl))
print(result)
result = list(map(lambda x:(x%2),nl))
print(result)

