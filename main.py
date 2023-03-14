"""ВЫЧИСЛЕНИЕ ИНТЕГРАЛОВ"""
import math as math

print("Введите нижнюю гарницу интегрирования:")
LOWER_LIMIT = int(input())
print("Введите вернюю границу интегрирования:")
UPPER_LIMIT = int(input())
if LOWER_LIMIT >= UPPER_LIMIT:
    print("Значения введены не прваильно, поэтому они будут заменены на 5 и 15")
    LOWER_LIMIT = 5
    UPPER_LIMIT = 15
print('Введите желаемый шаг:')
STEP = int(input())
if STEP <= 0:
    print("Шаг будет заменен на стандартный")
    STEP = 1
def n_kr(n):
    while n % 4 != 0:
        n = n + 1
    return n

def f(x):
    return (1/(1+(math.e)**(-0.6*(x-10))))+0.2

def right_method():
    summa = 0
    i = LOWER_LIMIT
    while(i < UPPER_LIMIT):
        summa = f(i) * STEP + summa
        i = i + STEP
    try:
        file = open("input.txt", 'a', encoding="utf-8")
        file.write(f'Метод правого прямоугольника(шаг = {STEP}) Результат = {summa}\n')
    finally:
        file.close()

def left_method():
    summa = 0
    i = LOWER_LIMIT + 1
    while(i < UPPER_LIMIT+1):
        summa = f(i) * STEP + summa
        i = i + STEP

    try:
        file = open("input.txt", 'a', encoding="utf-8")
        file.write(f'Метод левого прямоугольника(шаг = {STEP}) Результат = {summa}\n')
    finally:
        file.close()

def middle_method():
    summa = 0
    i = LOWER_LIMIT + 0.5
    while(i < UPPER_LIMIT):
        summa = f(i) * STEP + summa

        i = i + STEP

    try:
        file = open("input.txt", 'a', encoding="utf-8")
        file.write(f'Метод среднего прямоугольника(шаг = {STEP}) Результат = {summa}\n')
    finally:
        file.close()
def trap_method():
    summa = 0
    i = LOWER_LIMIT
    while i < UPPER_LIMIT:
        summa = ((f(i)+f(i+1))*STEP)/2 + summa
        i = i + STEP

    try:
        file = open("input.txt", 'a', encoding="utf-8")
        file.write(f'Метод трапеции (шаг = {STEP}) Результат = {summa}\n')
    finally:
        file.close()


def sympson():
    x0 = LOWER_LIMIT
    xn = UPPER_LIMIT
    n = STEP
    h = (xn - x0) / n
    integration = f(x0) + f(xn)

    for i in range(1, n):
        k = x0 + i * h

        if i % 3 == 0:
            integration = integration + 2 * f(k)
        else:
            integration = integration + 3 * f(k)

    # Finding final integration value
    integration = integration * 3 * h / 8

    try:
        file = open("input.txt", 'a', encoding="utf-8")
        file.write(f'Метод симпсона (шаг = {STEP}) Результат = {integration}\n')
    finally:
        file.close()

print('Введите цифру,которая соответсвует желаемому методу нахождения интеграла\n'
      '1 - Метод правого прямоугольника\n'
      '2 - Метод левого прямоугольника\n'
      '3 - Метод среднего прямоугольника\n'
      '4 - Метод Симпсона\n'
      '5 - Метод трапеции\n' )
choice = int(input())
if choice == 1:
    right_method()
if choice == 2:
    left_method()
if choice == 3:
    middle_method()
if choice == 4:
    sympson()
if choice == 5:
    trap_method()
print("Успех,результат занесен в файл")



