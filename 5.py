string = input("Введите строку: ")
str1 = ""
list_= list(string)
for i in range(len(list_)):
    list_[i] = list_[i].replace('a', '').replace('e', '').replace('o', '')
    str1 += list_[i]
print(str1)