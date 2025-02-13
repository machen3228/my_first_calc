"""The simple calculator code"""

import time
from decimal import Decimal, getcontext, InvalidOperation

getcontext().prec = 20


def summ(num1, num2):
    return num1 + num2


def substruct(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        return None
    return num1 / num2


def calculator():
    time.sleep(1)
    print('Выберете операцию\n'
          '1 - сложение\n'
          '2 - вычитание\n'
          '3 - умножение\n'
          '4 - деление'
          )

    selection = input('Введите номер операции: ')

    if selection in ['1', '2', '3', '4']:
        try:
            num1 = Decimal(input('Введите первое число: '))
            num2 = Decimal(input('Введите второе число: '))
        except InvalidOperation:
            print('Ошибка ввода. Пожалуйста, введите число')
            return None

        if selection == '1':
            result = summ(num1, num2)
            print(f'{num1} + {num2} = {result}')
        elif selection == '2':
            result = substruct(num1, num2)
            print(f'{num1} - {num2} = {result}')
        elif selection == '3':
            result = multiply(num1, num2)
            print(f'{num1} * {num2} = {result}')
        else:
            result = divide(num1, num2)
            if result is None:
                print('Нельзя делить на ноль, иначе вселенной придет конец')
            else:
                print(f'{num1} / {num2} = {result}')
    else:
        print('Неверный ввод')


if __name__ == '__main__':
    print('Добро подаловать в калькулятор!')
    while True:
        choice = input('Запустить калькулятор? ("y"(да) / "n"(нет)): ')
        if choice == 'y':
            calculator()
        elif choice == 'n':
            print('Спасибо за использование калькулятора. До свидания!')
            break
        else:
            print('Неверный ввод. Пожалуйста, введите "y" или "n".')
