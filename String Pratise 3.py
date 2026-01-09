
folder = "my_data"
path = fr"C:\{folder}\test.txt"
print(path)

s="ABC"
print(s)
print(type(s))
print(s[0])

b=b"ABC"
print(b)
print(type(b))
print(b[0])

print('I\'m \"OK\"!')
print('I\'m ok.')

print('I\'m learning\nPython.')
print('\\\n\\')

print('-------------')
print('\\\t\\')
print(r'\\\t\\')
# \t 会自动寻找下一个 8（或 4）字符的对齐点,“跳向下一个停车位”**
print("ID\t姓名\t\t分数")
print("--\t----\t\t----")
print("01\t张三\t\t95")
print("02\t欧阳锋\t\t88")  # 即使名字长短不一，分数也会尽量对齐

price1 = 5.5
price2 = 1250.0

print(f"商品A价格: {price1:<10} 元")
print(f"商品B价格: {price2:<10} 元")


print(f"商品A价格: {price1:>10} 元")
print(f"商品B价格: {price2:>10} 元")

print(f"商品A价格: {price1:^10} 元")
print(f"商品B价格: {price2:^10} 元")




name = "Apple"
price = 5.5
status = "Success"

# 这是一行，但包含了三个独立的“预留领土”
# 领土1: 10位左对齐 | 领土2: 8位右对齐 | 领土3: 12位居中对齐
print(f"|{name:<10}|{price:>8.2f}|{status:^12}|")


n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s33='''Hello,\n
Bob!'''
s4 = r'''Hello,\n
Bob!'''

# 执行打印
print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s33)

print(s4)


print(ord('A'))
print(chr(65))
print(ord('\u4e2d'))
print(ord('中'))
print(chr(25991))
print(chr(20013))


#Formatting Pratise
template="The %s index closed at %d points today"
print(template %("CS1 300",3900))
print(template %("S&P 500",5200))

index_name1="CS1 300"
points1=3900
index_name2="S&P 500"
points2=5200
print(f"The {index_name1} index closed at {points1} points today")
print(f"The {index_name2} index closed at {points2} points today")
#f=formatted r=row b=bytes

#  :(Colon)pratise
pi=3.14159
print(f"{pi:.2f}")
print(f"{0.123456:.1%}")

balance=500000000
print(f"saving:{balance:,}")#每隔三位数字加一个逗号,千分位分隔符

print(f"|{'apple':>10}|")
print(f"|{'apple':^10}|")
print(f"|{'apple':<10}|")

print(f"{'finance sheet':*^20}")
print(f"{'finance sheet': ^20}")
print(f"{'finance sheet':^20}")#效果同上



