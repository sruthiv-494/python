# try:
#     # x=10/0
#     b=10/2
# except ZeroDivisionError:
#     print("error")
# else:
#     print("success")
# finally:
#     print("cleanup")

# class InvalidAgeError(Exception):
#     pass
# def check_age(age):
#     if age<18:
#         raise InvalidAgeError("Age must be 18+")
#     else:
#         print("Eligible")
# check_age(27)

# try:
#     x=5/0
# except ZeroDivisionError:
#     print("error")
# else:
#     print(x)

# try:
#     num=int(input("Enter an integer : "))
# except ValueError:
#     print("Number is not an integer")
# else:
#     print("Integer")

# try:
#     with open("new.txt","r") as f:
#         print(f.read())
# except FileNotFoundError:
#     print("File not found...")

# try:
        
#         while True:
#             a=int(input("Enter a : "))
#             b=int(input("Enter b : "))
# except ValueError:
#         print("error")

# try:
#     with open("text.txt","w") as f:
#         content=f.read()
#         print(content)
# except PermissionError:
#     print("Not allowed to open the file...")

# try:
#     num=[1,2,3,4]
#     index=int(input("Enter index: "))
#     res=num[index]
# except IndexError:
#     print("Index out of range")
# else:
#     print(num[index])

# try:
#     num=[1,2,3,4]
#     res=num.len
#     print(res)
# except AttributeError:
#     print("List does not have len attribute")

# try:
#     x=10/0
# except ArithmeticError:
#     print("error")

# try:
#     num=int(input("Enter an integer : "))
#     print(num)
# except KeyboardInterrupt:
#     print("Input cancelled by the user")







    




