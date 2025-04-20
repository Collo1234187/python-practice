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
print()

#object oriented programming
  #class and object
class Dog:
  def __init__(self, name, age):
    self.name = name 
    self.age = age
  def bark(self):
    return f"{self.name} says Woof!"
# Creating an object 
my_dog = Dog("Buddy", 3) 
print(my_dog.name)  
print(my_dog.bark())
print() 

 #encapsulation
class BankAccount:
  def __init__(self, balance): 
    self.__balance = balance  # Private attribute
  def deposit(self, amount):
    if amount > 0: 
      self.__balance += amount
  def withdraw(self, amount):
    if amount > 0 and amount <= self.__balance:
      self.__balance -= amount
    else: 
      print("Insufficient funds")
  def get_balance(self): 
    return self.__balance
account = BankAccount(1000) 
account.deposit(5000)
account.withdraw(4000)
print(f"your account balance is {account.get_balance()}")
print()

 #inheritance
class Animal:
  def __init__(self, name):
    self.name = name
    def speak(self): 
      pass
class Dog(Animal):
  def speak(self): 
    return f"{self.name} says Woof!"
class Cat(Animal):
  def speak(self):
    return f"{self.name} says Meow!"
def animal_sound(Animal):
  return Animal.speak()
dog = Dog("Buddy") 
cat = Cat("Whiskers")
print(dog.speak()) 
print(cat.speak()) 
#polymorphism
print(animal_sound(dog))  
print(animal_sound(cat))
print()

#method overriding
class Vehicle:
  def __init__(self, name):
    self.name = name
  def start(self):  
    return f"{self.name} is starting."
class ElectricCar(Vehicle):
  def start(self): 
    return f"{self.name} is starting silently."
car = Vehicle("Generic Car") 
tesla = ElectricCar("Tesla Model 3")
print(car.start()) 
print(tesla.start()) 
print()


#multiple inheritance
class Flyable: 
  def fly(self): 
    return "I can fly!"
class Swimmable:
  def swim(self): 
    return "I can swim!"
class Duck(Animal, Flyable, Swimmable): 
  pass
duck = Duck("Donald") 
print(duck.fly())    
print(duck.swim())
print()   

#Class and Static Methods
class Person: 
  count = 0
  def __init__(self, name): 
    self.name = name 
    Person.count += 1
  @classmethod
  def get_count(cls):
    return cls.count

person1 = Person("Alice") 
person2 = Person("Bob") 
print(Person.get_count())  

#Static Methods
class MathOperations: 
  @staticmethod 
  def add(x, y):
    return x + y 
print(MathOperations.add(5, 3))  
print()

#Property Decorators
class Temperature:
  def __init__(self, celsius):
    self._celsius = celsius
  @property
  def celsius(self):
    return self._celsius
  @celsius.setter 
  def celsius(self, value):
    if value <= -273.15:
      raise ValueError("Temperature below absolute zero is not possible") 
    self._celsius = value
  @property
  def fahrenheit(self):
    return (self.celsius * 9/5) + 32
temp = Temperature(-273.15) 
print(temp.celsius)     
print(temp.fahrenheit)  
temp.celsius = 90
print(temp.celsius)   
print()

#FILE HANDLING
#open(filename, mode) 
#file = open('example.txt', 'r') # Perform operations on the 
#file.close()  # Always close the file when done
#File Opening Modes
#	'r': Read (default mode)
	#'a': Append (adds to the end of the file)
	#'x': Exclusive creation (fails if the file already exists)
	#  '+': Read and write mode

#reading from file
file=open('Document.txt', 'r')  
content = file.read() 
print(content)
file.close()
print()

#reading line by line
file = open('Document.txt', 'r') 
for line in file: 
  print(line.strip())  # strip() removes leading/trailing whitespace
file.close()
print()


#Reading Specific Number of Characters python
file=open('Document.txt', 'r') 
chunk = file.read(100)  # Read 100 characters 
print(chunk)
file.close()
print()

#writing in file
#Writing Strings 
file= open('Document.txt', 'w')  
file.write("Hello, World!\n") 
file.write("This is a new line.")

#Writing Multiple Lines 
#lines = ["Line 1\n", "Line 2\n", "Line 3\n"] 
#file= open('output.txt', 'w')  
#file.writelines(lines)

#Appending to Files
file=open('Document.txt', 'a') 
file.write("New log entry\n")

#Working with CSV Files
#Reading CSV Files 
#import csv
#file=open('data.csv', 'r') 
#csv_reader = csv.reader(file) 
#for row in csv_reader: 
#  print(row)

#Writing CSV Files python import csv
#data = [
#['Name', 'Age', 'City'],
#['Alice', '30', 'New York'],
#['Bob', '25', 'Los Angeles']
#]
#file=open('output.csv', 'w', newline='')
#csv_writer = csv.writer(file) 
#csv_writer.writerows(data)

#Working with JSON Files
#Reading JSON Files python 
#import json
#file=open('data.json', 'r') 
#data = json.load(file) 
#print(data)

#Writing JSON Files python 
'''import json
data = {
"name": "Alice",
"age": 30,
"city": "New York"
}
file=open('output.json', 'w')
json.dump(data, file, indent=4)'''

#Working with Binary Files
#Reading a binary file 
'''file = open('image.jpg', 'rb') 
content = file.read()
# Writing to a binary file with 
file=open('copy.jpg', 'wb')
file.write(content)'''

#File and Directory Operations
'''import os
# Get current working directory 
print(os.getcwd())
# List files and directories 
print(os.listdir())
# Create a new directory 
os.mkdir('new_directory')
# Rename a file 
os.rename('old_name.txt', 'new_name.txt')
# Delete a file 
os.remove('file_to_delete.txt')
# Check if a file exists 
print(os.path.exists('example.txt'))'''











