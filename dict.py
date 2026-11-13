d={"name":"sneha","age":23}

d["grade"]="A"
print(d)
d["age"]=12
print(d)

d.update({"place":"chennai","blood":"AB+"})
print(d)

print(d.get("age"))
print(d.keys())
print(d.values())
print(d.items())

del d["age"]

age=d.pop("age")
print(d)

last_item=d.popitem()
for key,value in d.items():
    print(f"{key}-->{value}")
print(d)

d.clear()
print(d)