n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()

n=4
for i in range(n):
    for j in range(2*i+1):
         print("*", end=" ")
    print()

for i in range(1,6):
    if i==2:
        continue
    if i==4:
        break
    print(i)


    