##Homework:

1.Given a side of square. Find its perimeter and area.

2.Given diameter of circle. Find its length.

3.Given two numbers a and b. Find their mean.

4.Given two numbers a and b. Find their sum, product and square of each number.
  
# 1-PUZZLE
  
a = int(input('Kvadratning yuzi va uning peremetrini toping:'))
S = a ** 2
P = 4 * a
print('Kvadratning yuzi:',S)
print('Kvadratning peremetri:',P)

# 2-PUZZLE


import math
r = int(input('Doiraning uzunligini toping:'))
L = 2 * math.pi * r
print('Doiraning uzunligi:',L)

# 3-PUZZLE


a = 5
b = 7
print('Mean value',(a + b)/2)

# 4-PUZZLE


a = int(input('a sonni kiriting:'))
b = int(input('b sonni kiriting:'))

sum_ab = a + b
product_ab = a * b
square_a = a ** 2
square_b = b ** 2

print('Ikkita sonning yigindisi',sum_ab)
print('Ikkita sonning kopaytmasi',product_ab)
print('a sonining kvadrati',square_a)
print('b sonining kvadrati',square_b)

