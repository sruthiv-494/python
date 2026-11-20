# l=[10,5]
# diff=lambda x,y : x-y
# print(diff(40,30))

# l=[1,2,3]
# s=list(map(lambda i:str(i),l))
# print(s)

# l=[15,23,55,22,11]
# d=list(filter(lambda i : i%10 == 5,l))
# print(d)

# num=[(1,2),(3,1),(5,4)]
# s=sorted(num,key=lambda i:i[1])
# print(s)

# s='happy'
# check=lambda i : 'a' in i
# print(check(s))


# check=lambda a,b,c : a*b*c
# print(check(1,2,3))

# l=[121,345,1221,456]
# p=list(filter(lambda n:str(n)==str(n)[::-1],l))
# print(p)

# l=[1,2,3]
# add=list(map(lambda i : i+10 , l))
# print(add)

# name={'apple':1,'mango':3, 'grapes':4,'banana':2}
# s=dict(sorted(name.items() , key=lambda item : item[0][0]))
# print(s)

# check=lambda x : x<50 and x>10
# print(check(20))

from functools import reduce
l=[1,2,3,4]
res=reduce(lambda a,b : a+b , l)
print(res)