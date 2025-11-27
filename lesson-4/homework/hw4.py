# Dictionary Exercises

# 1. Sort a Dictionary by Value
Write a Python script to sort (ascending and descending) a dictionary by value.

not_sorted_values = {5,7,8,10,9,15,1,3,6,4,12,14,13,2,11}

sorted_version_of_values = sorted(not_sorted_values)

print(sorted_version_of_values)

# 2. Add a Key to a Dictionary
Write a Python script to add a key to a dictionary.

keys_and_their_values = {0:10,1:20}

keys_and_their_values[2] = 30

print(keys_and_their_values)


# 3. Concatenate Multiple Dictionaries
Write a Python script to concatenate the following dictionaries to create a new one.
  
dict1 = {"a":1,"b":2,"c":3}

dict2 = {"d":4,"e":5,"f":6}

new_dict_in_one = {**dict1,**dict2}

print(new_dict_in_one)

# 4. Generate a Dictionary with Squares
Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

numbers = {1,2,3,4,5,6,7}

squared_version_of_numbers = {x:x**2 for x in numbers}

print(squared_version_of_numbers)

# 5. Dictionary of Squares (1 to 15)
Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
  
numbers = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}

squared_version_of_numbers = {x:x**2 for x in numbers}

print(squared_version_of_numbers)

# Set Exercises

# 1. Create a Set
Write a Python program to create a set.
  
smth_set = {"I love Xorazm"}

print(smth_set)


# 2. Iterate Over a Set
Write a Python program to iterate over sets.
  
my_set = {1,2,3,4,5,6,7}

for element in my_set:
    print(element)
  
# 3. Add Member(s) to a Set
Write a Python program to add member(s) to a set.
  
member_names = {"Murod","Eldor"}

member_names.update(["Mirshod","E'zozbek","Usmonbek"])

print(member_names)

# 4. Remove Item(s) from a Set
Write a Python program to remove item(s) from a given set.
  
numbers = {1,2,3,4,5,6,7}

numbers.discard(3)

print(numbers)
# 5. Remove an Item if Present in the Set
Write a Python program to remove an item from a set if it is present in the set.
  
fruit_name = input("Setdagi xohlagan meva turidan birisini tanglang")

type_of_fruits = {"Banana","Apple","Strawbery","Ananas","Avocado"}

if fruit_name in type_of_fruits:
    type_of_fruits.discard(fruit_name)
    print("Siz tanlagan meva turi setdan muvaffaqiyatli o'chirildi",type_of_fruits)
else:
    print("Siz tanlagan meva turi setda mavjud emas")
