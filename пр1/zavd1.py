a = float(input ("Введіть а: "))
while (a < 1 or a > 100):
    a = float(input ("Введіть ще раз а: "))
b = int(input ("Введіть  b: "))
while (b < 1 or b > 100):
    b = int(input ("Введіть ще раз b: "))
if a < b:
    x = (2 * a / b + 1)
elif a == b:
    x = -445
else:
    x = (b + 5) / a
print("Результат обчислення виразу: " , x)