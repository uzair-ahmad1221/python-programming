# Student Management System
# Author: Uzair (Example)
# A simple console-based program to manage student records

import json

# File to store student data
DATA_FILE = "students.json"

# Load students from file
def load_students():
    try:
        with open(DATA_FILE, "r") as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []
    return students

# Save students to file
def save_students(students):
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)

# Display all students
def display_students(students):
    if not students:
        print("No students found.\n")
        return
    print("=== Student List ===")
    for i, student in enumerate(students, start=1):
        print(f"{i}. {student['name']} | Age: {student['age']} | Grade: {student['grade']}")
    print()

# Add a new student
def add_student(students):
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")
    student = {"name": name, "age": age, "grade": grade}
    students.append(student)
    print("Student added successfully.\n")

# Update a student
def update_student(students):
    display_students(students)
    if not students:
        return
    try:
        idx = int(input("Enter student number to update: ")) - 1
        if idx < 0 or idx >= len(students):
            print("Invalid student number.\n")
            return
        student = students[idx]
        print(f"Updating {student['name']}")
        student['name'] = input("Enter new name: ") or student['name']
        student['age'] = input("Enter new age: ") or student['age']
        student['grade'] = input("Enter new grade: ") or student['grade']
        print("Student updated successfully.\n")
    except ValueError:
        print("Invalid input.\n")

# Delete a student
def delete_student(students):
    display_students(students)
    if not students:
        return
    try:
        idx = int(input("Enter student number to delete: ")) - 1
        if idx < 0 or idx >= len(students):
            print("Invalid student number.\n")
            return
        removed = students.pop(idx)
        print(f"Deleted student: {removed['name']}\n")
    except ValueError:
        print("Invalid input.\n")

# Search student by name
def search_student(students):
    name = input("Enter name to search: ").lower()
    results = [s for s in students if name in s['name'].lower()]
    if results:
        print("=== Search Results ===")
        for student in results:
            print(f"{student['name']} | Age: {student['age']} | Grade: {student['grade']}")
    else:
        print("No student found with that name.")
    print()

# Main menu
def main_menu():
    students = load_students()
    while True:
        print("=== Student Management System ===")
        print("1. Display all students")
        print("2. Add student")
        print("3. Update student")
        print("4. Delete student")
        print("5. Search student")
        print("6. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            display_students(students)
        elif choice == "2":
            add_student(students)
            save_students(students)
        elif choice == "3":
            update_student(students)
            save_students(students)
        elif choice == "4":
            delete_student(students)
            save_students(students)
        elif choice == "5":
            search_student(students)
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.\n")

# Run the program
if __name__ == "__main__":
    main_menu()

# ---------------------------------------------------------
# This program implements a CRUD-based student management system
# using lists, dictionaries, JSON file storage, functions, loops,
# and clear menu-based user interaction for practice purposes.
# ---------------------------------------------------------

# The total lines with comments and spacing will approach 200 if we expand
# with additional features like GPA calculation, sorting, data validation, etc.
# For practice, let's expand it with those additional features below.

# Calculate average age of students
def average_age(students):
    if not students:
        print("No students to calculate average age.\n")
        return
    total_age = sum(int(s['age']) for s in students)
    avg = total_age / len(students)
    print(f"Average age of students is: {avg:.2f}\n")

# Sort students by name
def sort_students_by_name(students):
    students.sort(key=lambda x: x['name'])
    print("Students sorted by name.\n")

# Sort students by grade
def sort_students_by_grade(students):
    students.sort(key=lambda x: x['grade'])
    print("Students sorted by grade.\n")

# Enhanced menu with sorting and average age
def enhanced_menu():
    students = load_students()
    while True:
        print("=== Enhanced Student Management System ===")
        print("1. Display all students")
        print("2. Add student")
        print("3. Update student")
        print("4. Delete student")
        print("5. Search student")
        print("6. Calculate average age")
        print("7. Sort students by name")
        print("8. Sort students by grade")
        print("9. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            display_students(students)
        elif choice == "2":
            add_student(students)
            save_students(students)
        elif choice == "3":
            update_student(students)
            save_students(students)
        elif choice == "4":
            delete_student(students)
            save_students(students)
        elif choice == "5":
            search_student(students)
        elif choice == "6":
            average_age(students)
        elif choice == "7":
            sort_students_by_name(students)
            save_students(students)
        elif choice == "8":
            sort_students_by_grade(students)
            save_students(students)
        elif choice == "9":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.\n")

# Uncomment below to run enhanced menu instead
# if __name__ == "__main__":
#     enhanced_menu()
