# Дан список имен.
# Выведите все имена в одну строку через запятую

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
string = ""

for name in names:
    string += name + ", "

print (string[:-2])

# Пример вывода:
# Иван, Ирина, Вячеслав, Василий, Петр
