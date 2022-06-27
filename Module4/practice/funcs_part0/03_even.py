def even (n):
    res = True
    if n % 2 != 0:
        res = False
    return res

n = ...
if even(n):
   print("Число четное")
else:
   print("Число не четное")
