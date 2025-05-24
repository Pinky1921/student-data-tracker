# -*- coding: utf-8 -*-
"""
Created on Sat May 24 21:13:43 2025

@author: Pinky
"""
import csv

# A list to store all student records
students = []

# Function to add a new student to the list
def add_student():
    """
    Adds a new student by taking their name, roll number, and marks for 3 subjects.
    The student data is stored in a dictionary and added to the global students list.
    """
    try:
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        marks = [float(input(f"Enter marks for subject {i+1}: ")) for i in range(3)]
        student = {"name": name, "roll": roll, "marks": marks}
        students.append(student)
        print("Student added successfully.\n")
    except ValueError:
        print("Invalid input. Marks should be numeric.\n")


# Function to display all student records
def display_students():
    """
    Displays all student records stored in the students list.
    Shows name, roll number, and marks. If no records exist, it shows a message.
    """
    if not students:
        print("No student records found.\n")
        return
    print("All Student Records:")
    for i, student in enumerate(students, 1):
        print(f"{i}. Name: {student['name']}, Roll: {student['roll']}, Marks: {student['marks']}")
    print()
    

# Function to calculate and display average marks for each student
def calculate_averages():
    """
    Calculates and displays average marks for each student.
    If the list is empty, notifies the user.
    """
    if not students:
        print("No student records to calculate averages.\n")
        return
    for student in students:
        avg = sum(student["marks"]) / len(student["marks"])
        print(f"Student: {student['name']} | Average Marks: {avg:.2f}")
    print()


# Function to save student records to a CSV file
def save_to_csv(filename="students.csv"):
    """
    Saves all student records to a CSV file with the given filename.
    Each row includes: name, roll number, and marks for 3 subjects.
    """
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Roll Number", "Subject1", "Subject2", "Subject3"])
            for student in students:
                writer.writerow([student["name"], student["roll"]] + student["marks"])
        print(f"Records saved to {filename} successfully.\n")
    except Exception as e:
        print(f"Error writing to file: {e}\n")


# Main menu to interact with the user
def menu():
    """
    Displays a menu with options to:
    1. Add Student
    2. Display All Students
    3. Calculate Average Marks
    4. Save to CSV File
    5. Exit Program

    Based on user's choice, the corresponding function is called.
    """
    while True:
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Calculate Average Marks")
        print("4. Save to CSV")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            calculate_averages()
        elif choice == '4':
            save_to_csv()
        elif choice == '5':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


# Start the program only if the script is run directly
if __name__ == "__main__":
    menu()

        print("Invalid input. Marks should be numeric.\n")


def display_students():
    if not students:
        print("No student records found.\n")
        return
    print("All Student Records:")
    for i, student in enumerate(students, 1):
        print(f"{i}. Name: {student['name']}, Roll: {student['roll']}, Marks: {student['marks']}")
    print()
    

def calculate_averages():
    if not students:
        print("No student records to calculate averages.\n")
        return
    for student in students:
        avg = sum(student["marks"]) / len(student["marks"])
        print(f"Student: {student['name']} | Average Marks: {avg:.2f}")
    print()

def save_to_csv(filename="students.csv"):
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Roll Number", "Subject1", "Subject2", "Subject3"])
            for student in students:
                writer.writerow([student["name"], student["roll"]] + student["marks"])
        print(f"Records saved to {filename} successfully.\n")
    except Exception as e:
        print(f"Error writing to file: {e}\n")

def menu():
    while True:
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Calculate Average Marks")
        print("4. Save to CSV")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            calculate_averages()
        elif choice == '4':
            save_to_csv()
        elif choice == '5':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    menu()
    
    
