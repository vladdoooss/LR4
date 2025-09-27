import math

# 1) Функція для обчислення z
def calc_z(m):
    return 1 / (math.sqrt(m) + math.sqrt(2))

# 2) Функція для перевірки простого числа
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# --- Головна частина програми ---
# Ввід m для першої функції
m = float(input("Введіть число m: "))
z = calc_z(m)
print("Значення z =", z)

# Ввід n для перевірки на простоту
n = int(input("Введіть число n: "))
if is_prime(n):
    print(n, "є простим числом")
else:
    print(n, "не є простим числом")