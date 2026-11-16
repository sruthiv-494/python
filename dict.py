# d={"name":"sneha","age":23}

# d["grade"]="A"
# print(d)
# d["age"]=12
# print(d)

# d.update({"place":"chennai","blood":"AB+"})
# print(d)

# print(d.get("age"))
# print(d.keys())
# print(d.values())
# print(d.items())

# del d["age"]

# age=d.pop("age")
# print(d)

# last_item=d.popitem()
# for key,value in d.items():
#     print(f"{key}-->{value}")
# print(d)

# d.clear()
# print(d)

# dict={"a":1 , "b":2 , "c":4}
# dict={k:v for k,v in dict.items() if v%2==0}
# print(dict)

# a={"a":1,"b":"sbs","c":"r","d":2.3}
# keys=[]
# for key,value in a.items():
#     if not isinstance(value,str):
#         keys.append(key)
# for key in keys:
#     del a[key]
# print(a)

# a={"a":7,"b":1,"c":4,"d":2}
# keys=[]
# for key,value in a.items():
#     if value%2 == 0:
#         keys.append(key)
# for key in keys:
#     del a[key]
# print(a)

# dict = {k : k**3 for k in range(1,5)}
# print(dict)

# str="mango is a fruit"

# dict={v : str.count(v)  for v in str if v in ['a','e','i','o','u'] }
# print(dict)
    
# word = {"apple"}
# dict = {k : k[::-1] for k in word}
# print(dict)
