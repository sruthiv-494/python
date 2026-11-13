marks=80
if marks>90:
    print("A")
elif marks>=80 and marks<90:
    print("B")
else:
    print("Failed")

username="admin"
password="123"
if username=="admin":
    print("OK")
    if password=="123":
        print("SUCCESS")
    else:
        print("FAILED")
else:
    print("NOT FOUND")

var=[1,2,3,4]
for i in var:
    print(i)
for i in range(10):
    print(i)


count=0
while count<3:
    print(count)
    count+=1


li=[1,2,3,4]
index=0
sum=0
while index < len(li):
    sum+=li[index]
    index+=1
print(sum)


