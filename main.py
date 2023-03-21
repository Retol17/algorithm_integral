"""ВЫЧИСЛЕНИЕ ИНТЕГРАЛОВ"""
from math import fabs,e



print("Введите нижнюю гарницу интегрирования:")
LOWER_LIMIT = int(input())
print("Введите вернюю границу интегрирования:")
UPPER_LIMIT = int(input())
if LOWER_LIMIT >= UPPER_LIMIT:
    print("Значения введены не прваильно, поэтому они будут заменены на 5 и 15")
    LOWER_LIMIT = 5
    UPPER_LIMIT = 15

def n_kr(n,UP,LOW):
    return (UP-LOW)/n


def f(x):
    return (1/(1+(e)**(-0.6*(x-10))))+0.2

def right_method(n):
    STEP = n_kr(n,UPPER_LIMIT,LOWER_LIMIT)
    summa = 0
    i = LOWER_LIMIT
    while(i < UPPER_LIMIT):
        summa = f(i) * STEP + summa
        i = i + STEP
    try:
        file = open("input.txt", 'a', encoding="utf-8")
        m = [f'{n}',f'{STEP}',f'{summa}',f'{7-summa}']
        file.write("{:<5}{:<10}{:<30}{:<30}\n".format(*m))
    finally:
        file.close()

def left_method(n):
    STEP = n_kr(n, UPPER_LIMIT, LOWER_LIMIT)
    summa = 0
    i = LOWER_LIMIT + 1
    while(i < UPPER_LIMIT+1):
        summa = f(i) * STEP + summa
        i = i + STEP

    try:
        file = open("input.txt", 'a', encoding="utf-8")
        m = [f'{n}', f'{STEP}', f'{summa}', f'{fabs(7 - summa)}']
        file.write("{:<5}{:<10}{:<30}{:<30}\n".format(*m))
    finally:
        file.close()

def middle_method(n):
    STEP = n_kr(n, UPPER_LIMIT, LOWER_LIMIT)
    summa = 0
    i = LOWER_LIMIT + 0.5
    while(i < UPPER_LIMIT):
        summa = f(i) * STEP + summa

        i = i + STEP

    try:
        file = open("input.txt", 'a', encoding="utf-8")
        m = [f'{n}', f'{STEP}', f'{summa}', f'{fabs(7 - summa)}']
        file.write("{:<5}{:<10}{:<30}{:<30}\n".format(*m))
    finally:
        file.close()
def trap_method(n):
    STEP = n_kr(n, UPPER_LIMIT, LOWER_LIMIT)
    summa = 0
    i = LOWER_LIMIT
    while i < UPPER_LIMIT:
        summa = ((f(i)+f(i+1))*STEP)/2 + summa
        i = i + STEP

    try:
        file = open("input.txt", 'a', encoding="utf-8")
        m = [f'{n}', f'{STEP}', f'{summa}', f'{fabs(7 - summa)}']
        file.write("{:<5}{:<10}{:<30}{:<30}\n".format(*m))
    finally:
        file.close()


def sympson(n):
    x0 = LOWER_LIMIT
    xn = UPPER_LIMIT
    STEP = n_kr(n, UPPER_LIMIT, LOWER_LIMIT)
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
        m = [f'{n}', f'{STEP}', f'{integration}', f'{fabs(7 - integration)}']
        file.write("{:<5}{:<10}{:<30}{:<30}\n".format(*m))
    finally:
        file.close()

print('Введите цифру,которая соответсвует желаемому методу нахождения интеграла\n'
      '1 - Метод правого прямоугольника\n'
      '2 - Метод левого прямоугольника\n'
      '3 - Метод среднего прямоугольника\n'
      '4 - Метод Симпсона\n'
      '5 - Метод трапеции\n' )
choice = int(input())
m = ['n','h','S','DS']
if choice == 1:
    try:
        file = open("input.txt", 'a', encoding="utf-8")

        file.write(f'Метод правого прямоугольника\n'
                   '{:<5}{:<10}{:<30}{:<30}\n'.format(*m))
    finally:
        file.close()
    right_method(10)
    right_method(20)
    right_method(40)
if choice == 2:
    try:
        file = open("input.txt", 'a', encoding="utf-8")

        file.write(f'Метод левого прямоугольника\n'
                   '{:<5}{:<10}{:<30}{:<30}\n'.format(*m))
    finally:
        file.close()
    left_method(10)
    left_method(20)
    left_method(40)
if choice == 3:
    try:
        file = open("input.txt", 'a', encoding="utf-8")

        file.write(f'Метод среденего прямоугольника\n'
                   '{:<5}{:<10}{:<30}{:<30}\n'.format(*m))
    finally:
        file.close()
    middle_method(10)
    middle_method(20)
    middle_method(40)

if choice == 4:
    try:
        file = open("input.txt", 'a', encoding="utf-8")

        file.write(f'Метод симпсона прямоугольника\n'
                   '{:<5}{:<10}{:<30}{:<30}\n'.format(*m))
    finally:
        file.close()
    sympson(10)
    sympson(20)
    sympson(40)
if choice == 5:
    try:
        file = open("input.txt", 'a', encoding="utf-8")

        file.write(f'Метод трапеции прямоугольника\n'
                   '{:<5}{:<10}{:<30}{:<30}\n'.format(*m))
    finally:
        file.close()
    trap_method(10)
    trap_method(20)
    trap_method(40)
else:
    print("Такого номера нет")
print("Успех,результат занесен в файл")



