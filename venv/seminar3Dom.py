# import random

#1
# numN = int(input("Введите кол-во чисел в массиве: "))
# numX= int(input("Введите число которое хотите проверить: "))
# count = 0
#
# list = []
#
# for i in range(numN):
#     list.append(random.randint(1,numN))
# print(list)
#
# for i in list:
#     if i == numX:
#         count +=1
# print(count)

#2
# numN = int(input("Введите кол-во чисел в массиве: "))
# numX= int(input("Введите число которое хотите проверить: "))
# num = 0
# temp = 0
# mintemp = 100
# list = []
#
# for i in range(numN):
#     list.append(random.randint(1,numN))
# print(list)
#
# for i in list:
#     temp = numX - i
#     if temp<0:
#         temp = temp * -1
#     if temp <= mintemp:
#         mintemp = temp
#         num = i
# print(f"Максимально близкое число: {num}")
#
# list_1 = [1, 2, 3, 4, 5]
# k = 6
# m = abs(k - list_1[0])  # модуль числа
# number = list_1[0]
# for i in range(1, len(list_1)):
#     if m > abs(list_1[i] - k):
#         m = abs(list_1[i] - k)
#         number = list_1[i]
# print(number)

#3
# word = input("Enter the word: ").upper()
# dict = {"AEIOULNSTRАВЕИНОРСТ": 1,"DGДКЛМПУ": 2, "BCMPБГЁЬЯ": 3, "FHVWYЙЫ": 4, "KЖЗХЦЧ": 5, "JXШЭЮ": 8, "QZФЩЪ": 10}
# count = 0
#
# for i in word:
#     for (k,v) in dict.items():
#         if i in k:
#             count += v
# print(count)

