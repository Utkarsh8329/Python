dict = {
    "Pankha":"Fan",
    "Khudchi":"chair"
}
# print(dict["khudchi"])
print("Dictionary have meaning of:")
for i in dict:
    print(i)
# print(dict.keys())
mean = input("Enter word for dictionary: ")
meaning = dict[mean]
print(meaning)