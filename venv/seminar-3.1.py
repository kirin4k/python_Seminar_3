import array
import random

# #1
# MAXNUM = 10
# MINNUM = 0
# list = []
# list_length = int(input("Введите длину списка: "))
#
# for i in range(list_length):
#     list.append(random.randint(MINNUM,MAXNUM))
# print(list)
# print(len(set(list)))

#2
# MAXNUM = 10
# MINNUM = 0
# list = []
# list_length = int(input("Введите длину списка: "))
# step = int(input("Введите шаг на который хотите сдвинуть: "))
# left_or_right = int(input("Введите 1 если хотите совершить сдвиг налево, 2 если на право: "))
# for i in range(list_length):
#     list.append(random.randint(MINNUM,MAXNUM))
# print(list)
#
# if left_or_right == 2:
#     for _ in range(step):
#         temp = list.pop()
#         list.insert(0,temp)
# else:
#     for _ in range(step):
#         temp = list.pop(0)
#         list.insert(len(list),temp)
# print(list)


# a = [1, 2, 3, 4, 5, 6]
# k = int(input("Введите число сдвигов: "))
# print(a)
# result = a[-k:] + a[:-k]
# print(result)
#3

# dict_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII ":"S007"}]
# uniq_el = set()
#
# for list_el in dict_list:
#     for key in list_el:
#         uniq_el.add(list_el[key])
# print(uniq_el)

# dict_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII ":"S007"}]
# uniq_el = set()
#
# for list_el in dict_list:
#     for value in list_el.values():
#         uniq_el.add(value)
# print(uniq_el)

#4
# MAXNUM = 10
# MINNUM = 0
# arr = []
# arr_length = int(input("Введите длину списка: "))
# for i in range(arr_length):
#     arr.append(random.randint(MINNUM,MAXNUM))
# print(arr)
#
# count = 0
# for i in range(arr_length - 1):
#     if arr[i] < arr[i+1]:
#         print(f"Элемент индексом - {i+1}, значением - {arr[i+1]} больше элемента индексом - {i}, значением - {arr[i]}")
#         count +=1
# print(f"Количество элементов больших предыдущего: {count}")

# count = 0
# for i in range(1, arr_length):
#     if arr[i] > arr[i-1]:
#         print(f"Элемент индексом - {i}, значением - {arr[i]} больше элемента индексом - {i-1}, значением - {arr[i-1]}")
#         count +=1
# print(f"Количество элементов больших предыдущего: {count}")
