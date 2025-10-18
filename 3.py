def process_and_print_list(data_list):
    print(f"Оригінальний список: {data_list}")
    # Створюємо тимчасовий список, щоб зібрати елементи з непарними індексами
    elements_to_add = []
    # Ітеруємо по індексах оригінального списку
    for i in range(len(data_list)):
        # Перевіряємо, чи індекс 'i' непарний
        if i % 2 != 0:
            elements_to_add.append(data_list[i])
    # Перевіряємо, чи ми взагалі щось знайшли
    if elements_to_add:
        print(f"\nЕлементи з непарними індексами: {elements_to_add}")
        # Доповнюємо основний список знайденими елементами
        data_list.extend(elements_to_add)
        print(f"Результат (доповнений список): {data_list}")
    else:
        print("\nУ списку немає елементів з непарними індексами (список занадто короткий).")

# Отримуємо список від користувача
# Користувач вводить елементи через пробіл, .split() робить з них список
input_string = input("Введіть елементи списку через пробіл: ")
my_list = input_string.split()
# Перевіряємо, чи список не порожній, і викликаємо функцію
if my_list:
    process_and_print_list(my_list)
else:
    print("Ви ввели порожній список.")