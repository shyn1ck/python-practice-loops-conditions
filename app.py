# Задача 1. Оценка студента и сравнение среднего значения

# 1) Напишите программу, которая запрашивает у пользователя его балл по экзамену и
# выводит сообщение оценки (A, B, C, D, F) в зависимости от полученного балла.
# Используйте следующий критерий:
# - A: 90-100
# - B: 80-89
# - C: 70-79
# - D: 60-69
# - F: менее 60
#
# 2) После вывода оценки, программа должна проверить, является ли оценка
# выше или ниже среднего значения (70). Если оценка выше среднего,
# программа должна вывести сообщение о том, что студент справился лучше среднего,
# а если оценка ниже среднего, сообщение о том, что студент справился хуже среднего.

# Решение
score = int(input("Введите ваш балл по экзамену: "))

# Определяем оценку по баллу
if 90 <= score <= 100:
    grade = "A"
elif 80 <= score <= 89:
    grade = "B"
elif 70 <= score <= 79:
    grade = "C"
elif 60 <= score <= 69:
    grade = "D"
else:
    grade = "F"

# Выводим оценку
print(f"Ваша оценка: {grade}")

# Проверяем, выше или ниже среднего значение
if score >= 70:
    print("Вы справились лучше среднего.")
else:
    print("Вы справились хуже среднего.")


# Задача 2. Обработка оценок студентов с использованием match...case
# 1) Напишите программу, которая запрашивает у пользователя его балл
# по экзамену и использует новую конструкцию match...case для
# определения оценки. Используйте следующий критерий:
#
# - A: 90-100
# - B: 80-89
# - C: 70-79
# - D: 60-69
# - F: менее 60
#
# 2) После вывода оценки, программа должна проверить, является ли
# оценка выше или ниже среднего значения (70). Если оценка выше среднего,
# программа должна вывести сообщение о том, что студент справился лучше среднего,
# а если оценка ниже среднего, сообщение о том, что студент справился хуже среднего
# Запрашиваем балл у пользователя
score = int(input("Введите ваш балл по экзамену: "))

# Используем конструкцию match...case для определения оценки
match score:
    case score if 90 <= score <= 100:
        grade = "A"
    case score if 80 <= score <= 89:
        grade = "B"
    case score if 70 <= score <= 79:
        grade = "C"
    case score if 60 <= score <= 69:
        grade = "D"
    case _:
        grade = "F"

# Выводим оценку
print(f"Ваша оценка: {grade}")

# Проверяем, выше или ниже среднего значение
if score >= 70:
    print("Вы справились лучше среднего.")
else:
    print("Вы справились хуже среднего.")


# Задача 3. Подсчет гласных и согласных
# 1) Создайте переменную `word`, которая содержит одно строковое значение (string) `analyst`;
# 2) Создайте цикл `for` для подсчета количества гласных (a, e, i, o, u) и выведите их количество на экран;
# 3) Используя цикл выведите на экран количество всех согласных букв из значения переменной (не включая гласные).
word = "salom"
vowels = "aeiou"

vowel_count = 0
consonant_count = 0

for char in word:
    if char in vowels:
        vowel_count += 1
    else:
        consonant_count += 1

print(f"Количество гласных в строке: {vowel_count}")
print(f"Количество согласных в строке: {consonant_count}")


# Задача 4. Поиск суммы чисел
# 1) Напишите программу на Python, используя цикл `while`,
# которая запрашивает у пользователя числа, суммирует их, и прекращает ввод, когда пользователь введет 0;
# 2) Выводите сумму введенных чисел на экран.

total_sum = 0
number = None

while number != 0:
    number = int(input("Введите число (для завершения введите 0): "))
    total_sum += number
print("Сумма введенных чисел:", total_sum)

# Задача 5. Путешествие по городам
# 1) Создайте кортеж city_destinations с названиями городов разных стран (например, 'Токио', 'Рим', 'Нью-Йорк', 'Сидней').
# Используйте итераторы, чтобы вывести на экран названия городов в следующем порядке:
# - Ваш первый город
# - Второй город в путешествии
# - Третий город, который вы посетите
# - Последний город в вашем путеводителе
#
# 2) Совершите ту же операцию с созданным кортежем используя цикл `for`.

city_destinations = ('Токио', 'Рим', 'Нью-Йорк', 'Сидней')
city_iterator = iter(city_destinations)

print("Ваш первый город:", next(city_iterator))
print("Второй город в путешествии:", next(city_iterator))
print("Третий город, который вы посетите:", next(city_iterator))
print("Последний город в вашем путеводителе:", next(city_iterator))

# Использование цикла for
city_destinations = ('Токио', 'Рим', 'Нью-Йорк', 'Сидней')

for index, city in enumerate(city_destinations):
    if index == 0:
        print("Ваш первый город:", city)
    elif index == 1:
        print("Второй город в путешествии:", city)
    elif index == 2:
        print("Третий город, который вы посетите:", city)
    elif index == 3:
        print("Последний город в вашем путеводителе:", city)



# Задача 6. Работа с массивом
# 1) Создайте массив, содержащий целые числа: `3, 7, 1, 9, 4, 8, 18, 28, 17, 31, 77, 95` и выведите его на экран.
# 2) Найдите среднее значение элементов массива и выведите результат на экран.
# 3)Добавьте новое значение в конец массива, например, `5555`. Выведите измененный массив на экран.
# 4)Удалите значение из массива, например, 9. Выведите измененный массив на экран


array = [3, 7, 1, 9, 4, 8, 18, 28, 17, 31, 77, 95]
print("Исходный массив:", array)

average = sum(array) / len(array)
print("Среднее значение элементов массива:", average)

array.append(5555)
print("Массив после добавления 5555:", array)

array.remove(9)
print("Массив после удаления 9:", array)


# Задача 7. Try-except
# 1) Напишите программу, которая запрашивает у пользователя два числа и выводит результат их деления.
# 2) Добавьте обработку ошибок с использованием конструкции try/except. Ваша программа должна обрабатывать следующие сценарии:
# - Если ввод пользователя не является числом, выведите сообщение об ошибке.
# - Если пользователь введет ноль в качестве знаменателя, выведите сообщение об ошибке и запросите ввод снова.

while True:
    try:
        numerator = float(input("Введите числитель: "))
        denominator = float(input("Введите знаменатель: "))
        result = numerator / denominator
    except ValueError:
        print("Ошибка: введите корректное число.")
        continue
    except ZeroDivisionError:
        print("Ошибка: деление на ноль невозможно. Попробуйте снова.")
        continue
    else:
        print(f"Результат деления: {result}")
        break
