# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

any_list = [-1, -4,  -21]

sum = 0

for element in any_list:
    if element > 0:
        sum += element

if sum > 0:
    print (f"Sum of positive numbers is {sum}")
else:
    print ("No positive numbers")
