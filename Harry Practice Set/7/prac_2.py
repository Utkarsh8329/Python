names = ["utkarsh","tikesh","pawan","yash"]
# for name in names:
#     print("Hello, ",name)
# else:
#     print("You are not invited")
name = input("Enter your name: ").lower()
if name in names:
    print("Hello, ",name,"my Dearsay")
else:
    print("You are not invited")