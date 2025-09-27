import math
from prime_module import is_prime   # імпортуємо нашу функцію з іншого модуля

# 1) Функція для обчислення z
def calc_z(m):
    return 1 / (math.sqrt(m) + math.sqrt(2))

# --- Головна частина програми ---
# Ввід m для першої функції
m = float(input("Введіть число m: "))
z = calc_z(m)
print(f"Значення z = {z}")

# Ввід n для перевірки на простоту
n = int(input("Введіть число n: "))
if is_prime(n):
    print(f"{n} є простим числом")
else:
    print(f"{n} не є простим числом")