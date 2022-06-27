# "Карточки"
# Для настольной игры используются карточки с номерами от 1 до N. Одна карточка потерялась.
# Найдите ее, зная номера оставшихся карточек.
# Вводится число N, далее еще N − 1 чисел: номера оставшихся карточек (различные числа от 1 до N).
# Программа должна вывести номер потерянной карточки.

cards_number = int(input("Enter number of cards "))
i = 1
sum1 = 0
sum2 = 0

while i <= cards_number-1:
    sum1 += int (input ("enter card number: "))
    sum2 = sum2 + i
    i +=1

sum2 +=i

#print (sum1)
#print (sum2)
print (f"Lost card has number {sum2 - sum1}")
