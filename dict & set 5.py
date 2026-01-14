import time
#age=input('age? ') #string <-------input（）
#age=int(age)
age=3
if age>=18:
    print("your age is",age)
    print('audlt')
elif age>=6:
    print('your age is',age)
    print('teenager')
else:
    print('kid')
    
score='dasjp'
match score:
    case 'a':
        print('score is a')
    case 'b':
        print('score is b')
    case 'c':
        print('score is c')
    case _:
        print('score is ???')

age=15
match age:
    case x if x<=10:
        print(f'<=10 years old:{x}')
    case 17:
        print('17 year old')
    case 11|12|13|14|15|18:
        print("11-16 and 18 year old")
    case _:
        print('not sure')
        
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name,end='',flush=True)#end=''禁止换行，把换行符号\n改为空
    time.sleep(0.8)
    
sum=0
for x in range(101):
    sum+=x
    print(sum)
    
sum2=0
n=99
while n>0:
    sum2=sum2+n
    n=n-2
print(sum2)

names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]
print(names[0],scores[0])

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

print(d.get('Thomas'))
print(d.get('Thomas', -1))#如果key不存在，可以返回None，或者自己指定的value
d.pop('Bob')
print(d)

s={1,2,3}
print(s)
s=set([1,2,3])
print(s)
s=set([1,1,2,2,3,3,1])
print(s)
s.add(4)
print(s)
s.remove(3)
print(s)

#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1={1,2,3}
s2={1,2,4}
print(s1&s2)
print(s1|s2)

a='abc'
b=a.replace("a","AA")
print(b)
