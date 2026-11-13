a=(1,2,3,4,5,6)
print(a.count(4))
print(a.index(5))
print(a)

b=list(a)
b[3]=10
print(b)

c=tuple(b)
print(c)

print(id(sorted(a)))
print(id(a))

