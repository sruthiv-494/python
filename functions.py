# li=[1,2,3,4,5]
# odd=[]
# for i in li:
#     if i%2 != 0:
#         odd.append(i)
# print(odd)

# def add(a,b):
#     return a+b
# print(add(3,5))

# def add(a,b,c=4):
#     return a+b-c
# print(add(50,b=20,c=20))

# def add_num(*args):
#     print(args)
#     print(sum(args))
# add_num(10,20,30)
# add_num(1,2,3,4)

# def num(a):
#     if a%2 == 0:
#       print(a , "is even")
#     else:
#        print(a, "is odd")
# num(47)

# x=4
# y=8
# a=lambda x,y:0.5*x*y
# print(a(x,y))

# x=10
# y=20
# sum=lambda x,y:x+y
# print(sum(x,y))

# l=[1,-10,2]
# output=list(filter(lambda x:x>0,l))
# print(output)

# stud=[("sneha",70),("sruthi",90),("anu",85)]
# res=sorted(stud,key=lambda stud:stud[1])
# print(res)

# def fact(n):
#     if n<=1:
#         return n
#     return n * fact(n-1)
# print(fact(5))


def fib(n):
    a=0
    b=1
    if n==1 or n==0:
        return n
    return fib(n-1) + fib(n-2)
for i in range(5):
    print(fib(i))
    
