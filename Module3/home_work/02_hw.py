# Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random
numbers = []
# print(random.randint(10, 20))  # раскомментируйте, чтобы посмотреть работу функции randint

import random

n = int (input ("Enter amount of numbers in the list: "))

any_list = []
i = 0

while i < n:
    number = random.randint(-100,100)
    any_list.append(number)
    i +=1

