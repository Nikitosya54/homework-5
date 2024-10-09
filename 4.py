from random import randint

list_ = []

for i in range(10):
    n = randint(1, 10)
    i = list_.append(n)

list_.clear()
print(list_)
