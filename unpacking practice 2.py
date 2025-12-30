#unpacking
point=(10,20,30)
x,y,z=point
print(x,y,z)

first,*other=[1,2,3,4,5]
print(first,other)

first,*middle,last=[1,2,3,4,5,6]
print(first,middle,last)

*other,middle,last=[1,2,3,4,5,6]
print(other,middle,last)

n=[1,2,3,4,5,6]
first,*_,last=n
print(first,_,last)