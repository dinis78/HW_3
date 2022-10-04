import os
from traceback import print_list
from unicodedata import name
os.system("cls")

# №1. Задайте список, состоящий из произвольных чисел
# количество задаёт пользователь. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётных
# позициях(не индексах).

import random
# num=int(input('Введите число '))
# num_list=[]
# for i in range(num):
#    num_list.append(random.randint(1,10))
# print(num_list)
# print(sum(num_list[::2]))  #срез, складываем элементы через один начиная с первого.

###############################################################

# №2. Напишите программу, которая найдёт произведение
# пар чисел списка. Парой считаем первый и последний
# элемент, второй и предпоследний и т.д.

# num=int(input('Введите число '))
# num_list=[]
# for i in range(num):
#    num_list.append(random.randint(1,10))
# print(num_list)
# my_list=[]
# for i in range((len(num_list)+1)//2):
#    my_list.append(num_list[i]*num_list[-1-i])
# print(my_list)

#####################################################################

# №3. Напишите программу, которая будет преобразовывать десятичное число в двоичное

# num = int(input('Введите целое число: ')) 
# x=format(num, 'b')  #Переводим в двоичное
# print(x)

#№ 4. Задайте список из вещественных чисел. Напишите программу, которая
# найдёт разницу между максимальным и минимальным значением дробной части элементов. 

my_list= [1.1, 1.2, 3.1, 5, 10.01]
new_list=[(num%1) for num in my_list if isinstance(num, float)]
print(new_list)
max_num=max(new_list)
min_num=min(new_list)
print('разница = ', round(max_num,2)-round(min_num,2))
