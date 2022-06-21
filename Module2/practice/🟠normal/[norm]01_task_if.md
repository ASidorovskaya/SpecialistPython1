## "Трехзначное ли"

### Задание

Проверьте, является ли данное число трехзначным.

### Формат входных данных

Дано целое число.

### Формат выходных данных

Вывести "Да", если данное число трехзначное и "Нет" в противоположном случае.

### Решение задачи

number = int (input("Enter number :"))

if number // 100 > 1:
    print ("Number consists of more than 3 numbers")
else:
    print ("Number consist of less than 3 numbers")

---
