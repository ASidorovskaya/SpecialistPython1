# Дан кортеж заполненный целыми числами
# Найдите самый большой элемент кортежа
tup = (2, 4, 6, -4, 12, 0, 5)

tup = (-2, -4, 2, -4, 12, -5)

max_tup = tup [0]

for number in tup:
    if number > max_tup:
        max_tup = number

print (f"Max number in tup = {max_tup}")
