# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

names = ["Иван", "Ирина", "Петр"]

max_len = 0
max_name = ""

for name in names:
    if len (name) > max_len:
        max_len = len (name)
        max_name = name

print (f"Max length of the name in the list is {max_len}\n Max name = {max_name}")
