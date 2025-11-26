# 1. Create and Access List Elements
Create a list containing five different fruits and print the third fruit.
  
name_of_fruits = ["Banana","Kiwi","Apple","Ananas","Avocado"]

selected_fruit = name_of_fruits[2]

print(selected_fruit)

# 2. Concatenate Two Lists
Create two lists of numbers and concatenate them into a single list.

a = [1,2,3,4,5]

b = [6,7,8,9,10]

a.extend(b)

print(a)

# 3. Extract Elements from a List
Given a list of numbers, extract the first, middle, and last elements and store them in a new list.

numbers = [1,2,3,4,5,6,7,8,9,10]

first_num = numbers[0]

middle_num = numbers[4]

last_num = numbers[-1]

selected_numbers = [first_num,middle_num,last_num]

print(selected_numbers)

# 4. Convert List to Tuple
Create a list of your five favorite movies and convert it into a tuple.
  
my_top_5_favourite_movies = ["Qashqirlar Makoni","Muqaddas Zamin","O'rgimchak odam","Matrix","Qora telefon 2"]

changed_to_tuple = tuple(my_top_5_favourite_movies)

print(changed_to_tuple)

# 5. Check Element in a List
Given a list of cities, check if "Paris" is in the list and print the result.
  
cities = ["Urganch","Tokio","Paris","Rome","Istanbul"]

if "Paris" in cities:
    print("Siz so'ragan shahar mavjud")
else:
    print("Afsuski sizning so'rovingizdagi shahar vaqtinchalik mavjud emas")
  
# 6. Duplicate a List Without Using Loops
Create a list of numbers and duplicate it without using loops.
numbers = [1,2,3,4,5,6,7]

duplicated = numbers * 2

print(duplicated)

# 7. Swap First and Last Elements of a List
Given a list of numbers, swap the first and last elements.

nums = [1,2,3,4,5,6,7]

nums[0],nums[6] = nums[6],nums[0]

print(nums)

# 8. Slice a Tuple
Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
num_1_10 = [1,2,3,4,5,6,7,8,9,10]

sliced_point = num_1_10[3:8]

print(sliced_point)

# 9. Count Occurrences in a List
Create a list of colors and count how many times "blue" appears in the list.
type_of_colors = ["Black","Blue","Red","Pink","Yello","Blue"]

amount_of_blue = type_of_colors.count("Blue")

print(amount_of_blue)

# 10. Find the Index of an Element in a Tuple
Given a tuple of animals, find the index of "lion".
type_of_animals = ["Tiger","Elephant","Snake","Bear","Fox","Lion","Zebra","Monkey"]

index_of_lion = type_of_animals.index("Lion")

print(index_of_lion)

# 11. Merge Two Tuples
Create two tuples of numbers and merge them into a single tuple.
a = (1,2,3,4,5)

b = (6,7,8,9,10)

two_tuples_in_one_tupple = a + b

print(two_tuples_in_one_tupple)

# 12. Find the Length of a List and Tuple
Given a list and a tuple, find and print their lengths.
smth_list = ["Banana","Kiwi","Avocado"]

smth_tuple = ("Apple","Ananas","Strawbery")

lenght_of_list = len(smth_list)

lenght_of_tuple = len(smth_tuple)

print("List uzunligi:",lenght_of_list)

print("Tuple uzunligi:",lenght_of_tuple)

# 13. Convert Tuple to List
Create a tuple of five numbers and convert it into a list.
numbers = (1,2,3,4,5)

tuple_changed_into_list = list(numbers)

print(tuple_changed_into_list)

# 14. Find Maximum and Minimum in a Tuple
Given a tuple of numbers, find and print the maximum and minimum values.
numbers = (600,707,667,702,699)

max_num = max(numbers)

min_num = min(numbers)

print(max_num)

print(min_num)

# 15. Reverse a Tuple
Create a tuple of words and print it in reverse order.


name_of_fruits = ("Banana","Kiwi","Apple","Ananas","Avocado")

reversed = name_of_fruits[::-1]

print(reversed)
