# На оси OX расположены 3 точки a,b,c. Определить, какая из точек b,c расположена ближе к а
from math import sqrt

entered_list = input().split()
num_list = list(map(int, entered_list))
AD = num_list[2] - num_list[0]
BD = num_list[3] - num_list[1]
AB = sqrt(AD**2 + BD**2)
AE = num_list[4] - num_list[0]
CE = num_list[5] - num_list[1]
AC = sqrt(AE**2 + CE**2)
if AB > AC:
    print("Точка c ближе к точке а")
elif AB == AC:
    print("Точка b совпадает с точкой с")
else:
    print("Точка b ближе к точке а")