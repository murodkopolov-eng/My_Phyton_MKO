# 1

def is_leap(year): """ Determines whether a given year is a leap year.

A year is a leap year if:
- It is divisible by 4, and
- It is NOT divisible by 100, unless it is also divisible by 400.

Parameters:
year (int): The year to be checked.

Returns:
bool: True if the year is a leap year, False otherwise.
"""
if not isinstance(year, int):
    raise ValueError("Year must be an integer.")

return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
determining_leap_year = int(input("Xohlagan yilni kiriting va biz sizga siz tanlagan yilda 29-fevral bormi yo'qmi shuni bilib beramiz"))

if (determining_leap_year % 4 == 0 and determining_leap_year % 100 != 0) or (determining_leap_year % 400 == 0):
    print("Siz so'ragan yilda 29-fevral mavjud")
else:
    print("Siz so'ragan yilda 29-fevral mavjud emas")
# 2
 Conditional Statements Exercise
Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
numbers_to_determine = int(input("Sonni kiriting"))

if numbers_to_determine % 2 != 0:
    print("Weird")
elif numbers_to_determine % 2 == 0 and 2 <= numbers_to_determine <= 5:
    print("Not Weird")
elif numbers_to_determine % 2 == 0 and 6 <= numbers_to_determine <= 20:
    print("Weird")
elif numbers_to_determine % 2 == 0 and numbers_to_determine > 20:
    print("Not Weird")
# 3
Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.
Give two solutions.

Solution 1 with if-else statement.

Solution 2 without if-else statement.
a = 7

b = 17

numbers = int(input("Berilgan oraliqdagi sonlardan birisini kiriting"))

if numbers % 2 != 0 and a <= numbers <= b:
    print("Toq son")
elif numbers % 2 == 0 and a <= numbers <= b:
    print("Juft son")




a = 7
b = 17

# Foydalanuvchidan sonlar ro'yxatini olish
numbers = list(map(int, input("Oraliqdagi sonlarni kiriting, bo‘sh joy bilan: ").split()))

# Juft sonlar (loopsiz)
even_numbers = [x for x in numbers if x % 2 == 0 and a <= x <= b]

# Toq sonlar (loopsiz)
odd_numbers = [x for x in numbers if x % 2 != 0 and a <= x <= b]

print("Juft sonlar:", even_numbers)
print("Toq sonlar:", odd_numbers)


