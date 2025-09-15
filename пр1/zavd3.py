# Введення числа N
N = int(input("Введіть число N (1 < N < 9): "))

# Перевірка, що N в допустимих межах
if 1 < N < 9:
    for i in range(N):
        for j in range(i + 1, N + 1):
            print(j, end=" ")
        print()  # перехід на новий рядок
else:
    print("Помилка: N повинно бути в межах від 2 до 8")