# написать программу которая получает 3 целых числа
# выводи на экран сначала максимальное затем минимальное а после оставшееся

a = int(input())
b = int(input())
c = int(input())

if a < b:
    a, b = b, a

if a < c:
    a, c = c, a

if b > c:
    b, c = c, b
print (a)
print (b)
print (c)