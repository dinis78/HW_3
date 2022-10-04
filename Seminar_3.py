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
# import random
num=int(input('Введите число '))
num_list=[]
for i in range(num):
   num_list.append(random.randint(1,10))
print(num_list)
my_list=[]
for i in range((len(num_list)+1)//2):
   my_list.append(num_list[i]*num_list[-1-i])
print(my_list)



