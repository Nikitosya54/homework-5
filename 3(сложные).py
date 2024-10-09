from random import randint
list_ = []
for i in range(10):
    n = randint(1, 10)
    i = list_.append(n)
print(list_)

list_.sort(reverse=True)
max1 = list_[0:1]
max2 = list_[1:2]
print(f"max1 = {max1}, max2 = {max2}")

