import math
#-----------Задача №11-------------------

def degrees2radians(degrees):
		result = degrees * math.pi / 180
		return result

a = 60
b = 45
c = 40
result =  math.cos(degrees2radians(60))
result2 = math.cos(degrees2radians(45))
result3 = math.cos(degrees2radians(40))
print('Result: %.2f, Result 2: %.2f, Result 3: %.2f' % (result, result2, result3))

#----------Задача №12--------------------

#---------Вариант Б-----------------
def sum_of_digits(number):
	result = int(number / 100) + int(number % 100 / 10) + (number % 10)
	return result

print(sum_of_digits(345))

#----------Вариант А----------------

def sum_of_digits2(number):
	number = str(number)
	result = int(number[0]) + int(number[1]) + int(number[2])
	return result

print(sum_of_digits2(123))

#--------Задача №13----------------

def cone_square_and_volume(radius, height):
		square = math.pi * radius * height
		volume = height / 3 * square
		return square,volume

print(cone_square_and_volume(2,7))





