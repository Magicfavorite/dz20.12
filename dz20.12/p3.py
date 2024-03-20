"""Пользователь вводит с клавиатурычисла. Если число
больше нуля нужно вывести надпись «Numberis positive»,
если меньше нуля «Numberis negative», если равно нулю
«Number is equal to zero». Когда пользователь вводит
на экран надпись «Good bye!»"""

while True:
    try:
        number = int(input("Введите число: "))
        if number > 0:
            print("Number is positive")
        elif number < 0:
            print("Number is negative")
        elif number == 0:
            print("Number is equal to zero")


        else:
            print("Введено некорректное значение. Пожалуйста, введите число."
                  "")
        if input("Хотите продолжить? (y/n): ") != 'y':
            
            print("Good bye!")
            break
    except ValueError:
        print("Введено некорректное значение. Пожалуйста, введите число.")
