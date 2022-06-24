# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

first_number = int(input("Enter first number: "))     # Первое число
second_number = int(input("Enter second number: "))    # Второе число

numbers_list = []

if first_number > second_number:
    first_number, second_number = second_number, first_number

list_number = first_number

while list_number  <= second_number:
    if list_number % 3 == 0:
        numbers_list.append(list_number)
    list_number +=1

if not numbers_list:
    print ("No numbers that can be divided by 3")
else:
    print (numbers_list)
