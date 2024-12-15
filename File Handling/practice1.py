#Practice Set 1
file = open("demo.txt", "r")
f = file.read()
if "just" in f:
    print("Just is present in demo file.")
else:
    print("Just is absent in demo file.")
file.close()