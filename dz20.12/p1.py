"""Пользователь вводит с клавиатурыдва числа. Нужно
посчитать отдельно сумму четных, нечетных и чисел,
кратных 9 в указанном диапазоне, а также среднеарифметическое каждой группы."""

while True:
    try:
        start = int(input("Введите начало диапазона: "))
        end = int(input("Введите конец диапазона: "))
        if start > end:
            raise ValueError
        even_sum = 0
        odd_sum = 0
        nine_sum = 0
        even_count = 0

        odd_count = 0

        nine_count = 0
        for number in range(start, end + 1):

            if number % 2 == 0:
                even_sum += number

                even_count += 1
            elif number % 2 != 0:
                odd_sum += number
                odd_count += 1

            if number % 9 == 0:
                nine_sum += number
                nine_count += 1
        even_average = even_sum / even_count if even_count != 0 else 0
        odd_average = odd_sum / odd_count if odd_count != 0 else 0
        nine_average = nine_sum / nine_count if nine_count != 0 else 0

        print(f"Сумма четных чисел: {even_sum}")
        print(f"Среднее арифметическое четных чисел: {even_average}")
        print(f"Сумма нечетных чисел: {odd_sum}")
        print(f"Среднее арифметическое нечетных чисел: {odd_average}")

        print(f"Сумма чисел, кратных 9: {nine_sum}")
        print(f"Среднее арифметическое чисел, кратных 9: {nine_average}")
        break
    except ValueError:
        print("Введено некорректное значение. Пожалуйста, введите начало и конец диапазона.")


