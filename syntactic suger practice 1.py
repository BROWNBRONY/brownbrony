#swap magic
x,y="apple","banana"
print(x,y)
x,y=y,x
print(x,y)
print(f"a is {x},b is {y}")

#f-sting interpolation 
price=99.5
count=3
print(f"Amount is: {price*count} doller")

#'''power
poem ='''
------------
Name:  YourName
Job:   Coder
------------
'''
print(poem)

#chain compair
age=25
if 18<=age<65:
    print("adult labor force")

#Conditional Expression
score=59
result="pass" if score >=60 else "false"
print (result)


#Digit Separator
money=1_000_000
print(money)

#List Comprehension
# [ 结果加工 | 循环取值 | 过滤条件 ]
# [for | in | if ]
squares=[x*x for x in range(1,6)] #fori=1 i<=5 i++{squares.add(i*i)}(java)
print(squares)
