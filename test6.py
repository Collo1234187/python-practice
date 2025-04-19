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