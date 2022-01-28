# логические операции
# and:
# True and True -> True
# False and true -> False
a = 23
b = 56
c = a > 10 and b <100
#print(c) ->true

# or 
# True or True -> True
# True or False -> True
# False or False -> False
a = 24
b = 24
c = a == b or a>100 or b<50
#print(c) -> True

#not
#not True -> False
#not False -> True
a = 23
c = a>10
# print (c) -> True
c = not a > 10
# print (c) -> False