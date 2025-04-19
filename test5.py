
#Real-World Scenario: Simple Quiz Game
questions = [
("What is the capital of France?", "Paris"),
("Which planet is known as the Red Planet?", "Mars"),
("What is 2 + 2?", "4")
] 
score = 0 
for question, correct_answer in questions: 
    user_answer = input(f"{question} ") 
    if user_answer.lower() == correct_answer.lower():
        print("Correct!") 
        score += 1
    else: 
        print(f"Sorry, the correct answer is {correct_answer}.") 
        print(f"\nYou got {score} out of {len(questions)} questions correct.")

#real world application for the data structures
contacts = []
def add_contact():
    name = input("Enter name: ") 
    phone = input("Enter phone number: ") 
    email = input("Enter email: ")
    contact = {"name": name, "phone": phone, "email": email} 
    contacts.append(contact) 
    print("Contact added successfully!")
def view_contacts():
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email:{contact['email']}")
def search_contact():
    search_term = input("Enter name to search: ") 
    for contact in contacts:
        if search_term.lower() in contact['name'].lower():
            print(f"Name: {contact['name']}, Phone: {contact['phone']},Email: {contact['email']}")
            return
            print("Contact not found.")
while True: 
    print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4.Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        break 
else: 
    print("Invalid choice. Please try again.") 
print("Thank you for using the Contact Book!")
