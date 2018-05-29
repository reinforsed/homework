import math

#_________________Задание 14_______________________


def is_even(number):
    if number % 2 == 0:
        print ('Четное число')
    else:
        print ('Нечетное число')

is_even(3)

#_______________Задание 15_________________________


def circles_intersect(x1, y1, r1, x2, y2, r2):
    dis = (x1 * x2) - (y1 * y2)
    sum_rad = r1 + r2
    if dis <= sum_rad and dis >= (r1 - r2):
        print('Пересекаються')
    else:
        print('Не пересекаються')

circles_intersect(1,2,3,4,5,6)


#______________Задание 16__________________________

def have_trains_crashed(v1, v2):
    time1 = 4 / v1
    time2 = 6 / v2
    if time1 < time2:
        print('No Crash')
    else:
        print('Crash')

have_trains_crashed(1,5)


#_____________Задание 17____________________________

def solve_quadratic_equation(a, b, c):
    square_root = b ** 2  - 4 * a *c
    if square_root < 0:
        print('No roots')
    elif square_root == 0:
        x = -b / (2 * a)
        print(x)
    else:
        x1 = (-b + math.sqrt(square_root)) / (2 * a)
        x2 = (-b - math.sqrt(square_root)) / (2 * a)
        print(x1)
        print(x2)

solve_quadratic_equation(1, 2, 3)








