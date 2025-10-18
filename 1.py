# Отримуємо довжину масиву (N)
n = 0
while True:
    try:
        n = int(input("Введіть кількість елементів у масиві (N): "))
        if n > 0:
            break
        else:
            print("Кількість елементів має бути більшою за нуль.")
    except ValueError:
        print("Будь ласка, введіть ціле число.")

# Створюємо порожній список (масив)
numbers = []

# Заповнюємо масив з клавіатури
print(f"\nБудь ласка, введіть {n} дійсних чисел (можна дробові):")
for i in range(n):
    while True:
        try:
            # Запитуємо елемент і додаємо його до списку
            value = float(input(f"Елемент {i + 1}: "))
            numbers.append(value)
            break
        except ValueError:
            print("Помилка! Будь ласка, введіть дійсне число (наприклад, 10 або -5.5).")

print(f"\nВаш масив: {numbers}")

print("\n--- Завдання 1: Середнє арифметичне непарних елементів ---")

odd_sum = 0.0
odd_count = 0

# Перебираємо масив по індексах
for i in range(len(numbers)):
    # Перевіряємо, чи індекс 'i' є непарним
    if i % 2 != 0:
        odd_sum += numbers[i]
        odd_count += 1

# Перевірка, чи були взагалі елементи на непарних позиціях
if odd_count > 0:
    average = odd_sum / odd_count
    print(f"Сума елементів на непарних позиціях: {odd_sum}")
    print(f"Кількість таких елементів: {odd_count}")
    print(f"Середнє арифметичне: {average:.2f}")
else:
    print("В масиві немає елементів на непарних позиціях (1, 3, 5...).")

print("\n--- Завдання 2: Від'ємні елементи у зворотному порядку ---")

# Створюємо список, куди зберемо всі від'ємні елементи
negatives = []
for num in numbers:
    if num < 0:
        negatives.append(num)

# Перевіряємо, чи ми щось знайшли
if negatives:
    print("Знайдені від'ємні елементи (у зворотному порядку):")

    # Використовуємо reversed() для ітерації по списку 'negatives' з кінця
    for neg_num in reversed(negatives):
        print(neg_num)
else:
    print("В масиві немає від'ємних елементів.")