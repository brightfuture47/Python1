﻿# является ли год високосным если да то вывести Високосный, если нет то обычный текст

year = int(input())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0: #Проверка кратности
    print ("Високосный")
else:
    print ("Обычный")
