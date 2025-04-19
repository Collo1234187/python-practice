#Variables and Data Types
age = 30 
height = 1.75 
name = "John Doe" 
is_student = False
print(f"Name: {name}, Age: {age}, Height: {height}m, Student: {is_student}")
print()

#Basic Operations
x = 10 
y = 3 
print(f"x + y = {x + y}") 
print(f"x - y = {x - y}") 
print(f"x * y = {x * y}") 
print(f"x / y = {x / y}") 
print(f"x // y = {x // y}") 
print(f"x % y = {x % y}") 
print(f"x ** y = {x ** y}") 
print(f"x == y: {x == y}") 
print(f"x != y: {x != y}") 
print(f"x > y and y < 5: {x > y and y < 5}")
print()

#if statement
age = 18 
if age >= 18: 
    print("You are eligible to vote.")
print()

#if else statement
age = 16 
if age >= 18:
    print("You are eligible to vote.")
else: 
    print("You are not eligible to vote yet.")
print()

#if-elif-else statement
score = 85 
if score >= 90: 
    print("Grade: A")
elif score >= 80: 
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else: 
    print("Grade: F")
print()

#for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits: 
    print(f"I like {fruit}")
print()

#for loop
for i in range(5):
    print(f"Iteration {i}")
print()

#while loop
count = 0 
while count < 5: 
    print(f"Count is {count}") 
    count += 1
print()

for num in range(4):
    if num == 5:
        break 
    print(num) 
else: 
    print("Loop completed normally")
print()

#Nested Control Structures
for i in range(3):
    for j in range(3):
        if i == j: 
            print("*", end=" ")
        else:
            print("0", end=" ")
print()
print()



#import module
import math 
print(math.pi)  
print()

#our own created import module
from math import sqrt 
print(sqrt(16)) 
print()

#creating your own module
import my_math
result = my_math.add(5, 3) 
print(result)

#function
def greet(name): 
    return f"Hello, {name}!"
message = greet("Alice") 
print(message)  
print()

#function and different ways of representing it
def describe_pet(animal_type, pet_name, age=1):
    return f"I have a {animal_type} named {pet_name}. It's {age} years old."
# Different ways to call the function 
print(describe_pet("dog", "Buddy")) 
print(describe_pet("cat", "Whiskers", 3))
print(describe_pet(pet_name="Rex", animal_type="dog", age=2))
print()

#return statement
def calculate_area(length, width): 
    return length * width
area = calculate_area(5, 3) 
print(f"The area is {area} square units.")
print()

#lambda function
square = lambda x:x**2   
print(square(4))  
print()

#function
def square(num):
    return num**2
Manipulation=square(3)
print(Manipulation)
print()

#the if __name__=="__main__": idiom
def main(): 
    print("This is the main function")
if __name__ == "__main__":
    main()
print()

#random module
import random
  # Generate a random number between 1 and 10 
number = random.randint(1, 10) 
print(f"Random number: {number}")
# Shuffle a list
my_list = [1, 2, 3, 4, 5] 
random.shuffle(my_list) 
print(f"Shuffled list: {my_list}")
print()

#data structures
  #list data structure
   #Empty list
empty_list = []
  #List of numbers 
numbers = [1, 2, 3, 4, 5]
  #List of mixed data types 
mixed = [1, "hello", 3.14, True]
  #List created using the list() constructor 
another_list = list("Python")
print(another_list)
print(numbers)
print(mixed)
print()

#Accessing List Elements
fruits = ["apple", "banana", "cherry"] 
print(fruits[0])
print(fruits[-2])  
print(fruits[1:3])  
print()

#List Operations python 
fruits = ["apple", "banana", "cherry"] 
  #Adding items
fruits.append("date")
print(fruits) 
fruits.insert(1, "blueberry")
print(fruits)
  #removing elements
fruits.remove("banana") 
print(fruits)
fruits.pop() 
print(fruits)
  #other operation
print(len(fruits) )
print(fruits.index("cherry"))
print(fruits.count("apple"))
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
print()

#List Comprehensions
squares = [x**2 for x in range(10)]
even_numbers = [x for x in range(20) if x % 2 == 0]
print(even_numbers)
print(squares)

#Tuples same as list but can not be modified
empty_tuple = () 
single_element = (1,)  # Note the comma
coordinates = (3, 4) 
mixed_tuple = (1, "hello", 3.14)
print(single_element)
print(mixed_tuple)
  #Accessing Tuple Elements 
print(coordinates[0])  
  #tuple operation
   # Concatenation 
combined = coordinates + (5, 6)
print(combined)
 # Repetition 
repeated = coordinates * 3
print(repeated)
 # Unpacking 
x, y = coordinates
print(x,y)
print()

#Dictionary also known as hash map in other programming language
  #Creating Dictionaries python
empty_dict = {}
person = {"name": "Alice", "age": 30, "city": "New York"} 
another_dict = dict(a=1, b=2, c=3)
print(person)
print(another_dict)
  #Accessing Dictionary Elements python
print(person["name"]) 
print(person["age"])
print(person.get("age"))
print(person.get("name"))
  # Using get() with a default value
print(person.get("country", "Unknown")) 
#Dictionary Operations python
  # Adding or updating elements 
person["occupation"] = "Engineer"
print(person) 
person.update({"married": True, "age": 31})
print(person) 
# Removing elements del person["city"] 
occupation = person.pop("occupation")
print(person)
# Other operations 
keys = person.keys() 
print(keys) 
values = person.values() 
print(values)
items = person.items()
print(items)
print()

#set
empty_set = set() 
numbers = {1, 2, 3, 4, 5} 
unique_chars = set("hello")
print(empty_set)
print(number)
print(unique_chars)
#Set Operations python
# Adding and removing elements
numbers.add(6)
print(numbers) 
numbers.remove(3)
print(numbers)
# Set operations 
set1 = {1, 2, 3, 4} 
set2 = {3, 4, 5, 6}
union = set1 | set2 
intersection = set1 & set2 
difference = set1 - set2 
symmetric_difference = set1 ^ set2
print(union)
print(difference)
print(symmetric_difference)



