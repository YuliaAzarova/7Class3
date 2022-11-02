# написать программу нахождения суммы большего и меньшего из 3 чисел

a = int(input())
b = int(input())
c = int(input())
list = [a, b, c]
list.sort()
print(list[0]+list[2])
