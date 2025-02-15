"""The simple calculator code"""

import time
from decimal import Decimal, getcontext, InvalidOperation

getcontext().prec = 6


class Calculator:

    def __init__(self, num1, num2):
        self.num1 = Decimal(num1)
        self.num2 = Decimal(num2)

    def summ(self):
        result = self.num1 + self.num2
        return result

    def substruct(self):
        result = self.num1 - self.num2
        return result

    def multiply(self):
        result = self.num1 * self.num2
        return result

    def divide(self):
        if self.num2 == 0:
            return None
        result = self.num1 / self.num2
        return result


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
            num1 = input('Введите первое число: ')
            num2 = input('Введите второе число: ')
            klass = Calculator(num1, num2)
        except InvalidOperation:
            print('Ошибка ввода. Пожалуйста, введите число')
            return None

        if selection == '1':
            result = klass.summ()
            print(f'{num1} + {num2} = {result}')
        elif selection == '2':
            result = klass.substruct()
            print(f'{num1} - {num2} = {result}')
        elif selection == '3':
            result = klass.multiply()
            print(f'{num1} * {num2} = {result}')
        else:
            result = klass.divide()
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
