# ============================= УВАГА! =============================
# Цей файл містить ПРИКЛАД виконання лабораторної роботи.
# Ваше завдання - розробити ВЛАСНУ програму згідно з вашим варіантом.
#
# Ви можете використовувати цей код як зразок, але не копіювати його.
# Повністю замініть цей код своєю реалізацією.
#
# Ваш код повинен відповідати таким вимогам:
# 1. Обрана предметна область згідно з вашим варіантом.
# 2. Реалізовано всі необхідні функції:
#    - додавання, видалення, оновлення даних
#    - пошук та фільтрація
#    - обчислення статистик (середнє, min/max)
#    - групування та агрегація
# 3. Використано map(), filter(), reduce(), сортування, зрізи.
# 4. Реалізовано операції з множинами та словниками.
# 5. Створено інтерактивне меню для користувача.
# =================================================================

from functools import reduce 

# Приклад: Аналіз даних про продажі
# ЗАМІНІТЬ ЦІ ДАНІ ТА ЛОГІКУ НА ВАШІ ВЛАСНІ

# Дані про погоду
weather = [
    {"city": "Київ", "temperature": 15, "rain": 2, "wind": 4},
    {"city": "Донецьк", "temperature": 12, "rain": 5, "wind": 6},
    {"city": "Одеса", "temperature": 19, "rain": 0, "wind": 3},
    {"city": "Дніпро", "temperature": 17, "rain": 1, "wind": 5},
    {"city": "Харків", "temperature": 14, "rain": 3, "wind": 7}
]

# 1. Виведення всіх даних
def show_weather():
    print("\n--- Дані про погоду ---")

    for item in weather:
        print(
            item["city"],
            "| Температура:", item["temperature"], "°C",
            "| Опади:", item["rain"], "мм",
            "| Вітер:", item["wind"], "м/с"
        )


# 2. Додавання нового запису
def add_weather():
    city = input("Введіть місто: ")
    temperature = float(input("Температура: "))
    rain = float(input("Кількість опадів: "))
    wind = float(input("Швидкість вітру: "))

    new_data = {
        "city": city,
        "temperature": temperature,
        "rain": rain,
        "wind": wind
    }

    weather.append(new_data)

    print("Дані додано.")

# 3. Видалення запису
def delete_weather():
    city = input("Введіть місто для видалення: ")

    for item in weather:
        if item["city"].lower() == city.lower():
            weather.remove(item)
            print("Дані видалено.")
            return

    print("Місто не знайдено.")

#4. Оновлення даних

def update_weather():
    city = input("Введіть місто: ")

    for item in weather:
        if item["city"].lower() == city.lower():

            item["temperature"] = float(input("Нова температура: "))
            item["rain"] = float(input("Нові опади: "))
            item["wind"] = float(input("Нова швидкість вітру: "))

            print("Дані оновлено.")
            return

    print("Місто не знайдено.")

#5. Пошук
def search_weather():
    city = input("Введіть місто: ")

    for item in weather:
        if item["city"].lower() == city.lower():

            print("\nЗнайдено:")
            print("Місто:", item["city"])
            print("Температура:", item["temperature"], "°C")
            print("Опади:", item["rain"], "мм")
            print("Вітер:", item["wind"], "м/с")

            return

    print("Місто не знайдено.")


#6. Фільтрація
def filter_weather():
    value = float(input("Показати міста з температурою вище: "))

    result = list(
        filter(lambda x: x["temperature"] > value, weather)
    )

    print("\nРезультат:")

    for item in result:
        print(item["city"], "-", item["temperature"], "°C")

#7. Статистика
def statistics():
    temperatures = list(
        map(lambda x: x["temperature"], weather)
    )

    average = sum(temperatures) / len(temperatures)

    print("\n--- Статистика ---")
    print("Середня температура:", round(average, 2), "°C")
    print("Мінімальна температура:", min(temperatures), "°C")
    print("Максимальна температура:", max(temperatures), "°C")

#8. Групування
def group_weather():
    groups = {
        "Холодно": [],
        "Тепло": []
    }

    for item in weather:

        if item["temperature"] < 15:
            groups["Холодно"].append(item["city"])
        else:
            groups["Тепло"].append(item["city"])

    print("\n--- Групування ---")

    for group in groups:
        print(group, ":", groups[group])


#9. map(), filter(), reduce()
def built_in_functions():

    # map - отримуємо список температур
    temperatures = list(
        map(lambda x: x["temperature"], weather)
    )

    # filter - міста без опадів
    no_rain = list(
        filter(lambda x: x["rain"] == 0, weather)
    )

    # reduce - сума опадів
    total_rain = reduce(
        lambda total, x: total + x["rain"],
        weather,
        0
    )

    print("\nТемператури:")
    print(temperatures)

    print("\nМіста без опадів:")

    for item in no_rain:
        print(item["city"])

    print("\nЗагальна кількість опадів:", total_rain, "мм")


#10. Сортування та зрізи
def sorting():

    sorted_weather = sorted(
        weather,
        key=lambda x: x["temperature"]
    )

    print("\nВід найхолоднішого до найтеплішого:")

    for item in sorted_weather:
        print(item["city"], item["temperature"], "°C")

    print("\nПерші 3 записи:")
    print(weather[:3])


#11. Множини та словники
def sets_and_dicts():

    # Створюємо множину міст
    cities = set()

    for item in weather:
        cities.add(item["city"])

    print("\nМножина міст:")
    print(cities)

    # Приклад двох множин
    set1 = {"Київ", "Львів", "Одеса"}
    set2 = {"Київ", "Дніпро", "Харків"}

    print("\nОб'єднання:")
    print(set1 | set2)

    print("Перетин:")
    print(set1 & set2)

    print("Різниця:")
    print(set1 - set2)

    # Словник для підрахунку температур
    temperature_count = {}

    for item in weather:
        temp = item["temperature"]

        if temp in temperature_count:
            temperature_count[temp] += 1
        else:
            temperature_count[temp] = 1

    print("\nЧастота температур:")
    print(temperature_count)


# Головне меню
while True:

    print("\n========== МЕНЮ ==========")
    print("1 - Показати всі дані")
    print("2 - Додати дані")
    print("3 - Видалити дані")
    print("4 - Оновити дані")
    print("5 - Пошук міста")
    print("6 - Фільтрація")
    print("7 - Статистика")
    print("8 - Групування")
    print("9 - map(), filter(), reduce()")
    print("10 - Сортування та зрізи")
    print("11 - Множини та словники")
    print("0 - Вихід")

    choice = input("Оберіть дію: ")

    if choice == "1":
        show_weather()
    elif choice == "2":
        add_weather()
    elif choice == "3":
        delete_weather()
    elif choice == "4":
       update_weather()
    elif choice == "5":
        search_weather()
    elif choice == "6":
        filter_weather()
    elif choice == "7":
        statistics()
    elif choice == "8":
        group_weather()
    elif choice == "9":
        built_in_functions()
    elif choice == "10":
        sorting()
    elif choice == "11":
        sets_and_dicts()
    elif choice == "0":
        print("Програму завершено.")
        break
    else:  
    print("Невірний пункт меню.")
