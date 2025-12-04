# 2. Integer Squares Exercise


Task
The provided code stub reads an integer, n, from STDIN. For all non-negative integers i where 0 <= i < n, print i^2.
n = int(input("1dan 5gacha xohlagan son kiriting"))
if 0 <= n <= 5:
    for i in range(n):
        print(i ** 2)
else:
    print("Son faqat 5gacha bo'lishi shart!")
# 3. Loop-Based Exercises

Exercise 1: Print first 10 natural numbers using a while loop
number = 0
while number < 11:
    print(number)
    number += 1
Exercise 2: Print the following pattern

for i in range(1,6):
    for j in range(1,i + 1):
        print(j,end = "")
    print()
Exercise 3: Calculate sum of all numbers from 1 to a given number
total = sum(range(1,11))
print(total)
Exercise 4: Print multiplication table of a given number

for number in range(2,21):
    print(number)
    number += 1
Exercise 5: Display numbers from a list using a loop
numbers = [12, 75, 150, 180, 145, 525, 50]
favorite_numbers = [75,150,145]
for x in numbers:
    if x in favorite_numbers:
        print(x)           
Exercise 6: Count the total number of digits in a number
digits = 105102738600707878
changed_type_of_digits = [int(x) for x in str(digits)]
amount_of_digits = len(changed_type_of_digits)
print(amount_of_digits)
Exercise 7: Print reverse number pattern
n = int(input("Son kiriting"))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end = " ")
    print()
Exercise 8: Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]
for elements in list1[::-1]:
    print(elements)
    
Exercise 9: Display numbers from -10 to -1 using a for loop
for i in range(-10,0):
    print(i)
Exercise 10: Display message “Done” after successful loop execution
for i in range(0,5):
    print(i)
print("Done!")
Exercise 11: Print all prime numbers within a range
for n in range(25,51):
    if n <= 1:
        print(f"{n} is not prime number")
    else:
        is_prime = True

        for i in range(2,n):
            if n % i == 0:
                print(f"{n} is not prime number")
                is_prime = False
                break
        if is_prime:
            print(f"{n} is prime number")
        else:
            print(f"{n} is not prime number")


        
        
Exercise 12: Display Fibonacci series up to 10 terms
first_num = 0
second_num = 1
for i in range(1,6):
    next_num = first_num + second_num
    print(next_num)
    first_num = second_num
    second_num = next_num

Exercise 13: Find the factorial of a given number
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))


4. Return Uncommon Elements of Lists
list1 = [1, 1, 2] 
list2 = [2, 3, 4]
uncommon_numbers = []
for num in list1:
    if num not in list2:
        uncommon_numbers.append(num)
for num in list2:
    if num not in list1:
        uncommon_numbers.append(num)
print(uncommon_numbers)  

list1 = [1, 2, 3]
list2 = [4, 5, 6]
common = list(set(list1) | set(list2))
print(common)
list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]
uncommon_numbers = []
for num in list1:
    if num not in list2:
        uncommon_numbers.append(num)
for num in list2:
    if num not in list1:
        uncommon_numbers.append(num)
print(uncommon_numbers) 
