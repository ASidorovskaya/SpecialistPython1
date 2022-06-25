# Дано 3 кортежа заполненные произвольными целыми числами.
# Найдите количество элементов, которые встречаются во всех трех кортежах.

tup1 = (-2, 2, -9, 12, -5)
tup2 = (3, -4, 2)
tup3 = (-2, 3, -4, 12, 2)


count = 0

for number in tup1:
    if number in tup2 and number in tup3:
        count +=1

print (f"Number of same numbers  = {count}")
