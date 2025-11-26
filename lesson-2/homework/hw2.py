# 1. Age Calculator
Write a Python program to ask for a user's name and year of birth, then calculate and display their age.

name = input("Ismingizni kiriting:")
birth_year = int(input("Tug'ilgan yilingizni kiriting:"))

current_year = 2025
age = current_year - birth_year

print("Mening ismim",name,"va men",age,"yoshdaman")

# 2. Extract Car Names
Extract car names from the following text:
txt = 'LMaasleitbtui'

txt = 'LMaasleitbtui'
selected1_car_name = txt[1::2]
print(selected1_car_name)

# 3. Extract Car Names
Extract car names from the following text:
txt = 'MsaatmiazD

txt = 'MsaatmiazD'
selected2_car_name = (txt[-1::-2],txt[0::2])
print(selected2_car_name)

# 4. Extract Residence Area
Extract the residence area from the following text:
txt = "I'am John. I am from London"

txt = "I'am John. I am from London"
area = txt.split()
selected_city = area[-1]
print(selected_city)

# 5. Reverse String
Write a Python program that takes a user input string and prints it in reverse order.

my_str = "I love coding"
reversed = my_str[::-1]
print(reversed)

# 6. Count Vowels
Write a Python program that counts the number of vowels in a given string.
  
my_region = "I love Xorazm"
vowels = "aeiouAEIOU"
count_available_vowels = sum(1 for letter in my_region if letter in vowels)
print("Unli harflar soni:",count_available_vowels)

# 7. Find Maximum Value
Write a Python program that takes a list of numbers as input and prints the maximum value.
  
price = [100,150,900,990,800,15]
max_value = max(price)
print(max_value)
# 8. Check Palindrome
Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).

word = input("Xohlagan harf kiriting va biz sizga bu so'z palindrommi yoki yo'qmi shuni aniqlab beramiz")
if word == word[::-1]:
    print("Bu so'z palindrom")
else:
    print("Bu so'z palindrom emas")
  
# 9. Extract Email Domain
Write a Python program that extracts and prints the domain from an email address provided by the user.

email = input("Iltimos emailingizni kiriting")
selected_point = email.split("@")[1]
print(selected_point)

# 10. Generate Random Password
Write a Python program to generate a random password containing letters, digits, and special characters.

import random
import string
letters = string.ascii_letters
digits = string.digits          
symbols = string.punctuation 
all_chars = letters + digits + symbols
password = "".join(random.choice(all_chars) for i in range(12))
print("Parol:", password)
