names = ["Anna", "Natasha", "Mike"]
names.insert(2, "Xi")
print(names)

#for x in range(1, 4):
#    print(int((str((float(x))))))

sample_dict = {1: 'Coffee', 2: 'Tea', 3: 'Juice'}
for x in sample_dict:
    print(x)


def recursion(num):
    print(num)
    next = num - 3
    if next > 1:
        recursion(next)

recursion(11)