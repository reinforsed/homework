import math

#------Задание №1------------------

a = 2
b = 3
c = 4
result = a + b * (c / 2)
print('Результатом выражения при: a = %d, b = %d, c = %d равен %.2f' % (a, b, c, result))

#------Задание №2------------------

a = 2
b = 3
result = (2**2 + 3**2) % 2
print('Результатом выражения при: a = %d, b = %d равен %.2f' % (a, b, result))

#-----Задание №3--------------------

a = 2
b = 3
с = 4
result = ( a + b ) / 12 * c % 4 + b
print('Результатом выражения при: a = %d, b = %d, c = %d равен %.2f' % (a, b, c, result))

#-----Задание №4---------------------

a = 2
b = 3
с = 4
result = (a - b * c ) / ( a + b ) % c
print('Результатом выражения при: a = %d, b = %d, c = %d равен %.2f' % (a, b, c, result))

#-----Задание №5---------------------

a = 2
b = 3
с = 4
result = math.fabs(a - b) /(( a + b) ** 3) - math.cos( c )
print('Результатом выражения при: a = %d, b = %d, c = %d равен %.2f' % (a, b, c, result))

#----Задание №6-----------------------

a = 2
b = 3
с = 4
result =  ((math.log( 1 + c ) / -b )**4) + math.fabs( a )
print('Результатом выражения при: a = %d, b = %d, c = %d равен %.2f' % (a, b, c, result))