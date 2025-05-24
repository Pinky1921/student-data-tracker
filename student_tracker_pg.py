# -*- coding: utf-8 -*-
"""
Created on Sat May 24 21:13:43 2025

@author: Pinky
"""

import csv

students = []

def add_student():
    try:
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        marks = [float(input(f"Enter marks for subject {i+1}: ")) for i in range(3)]
        student = {"name": name, "roll": roll, "marks": marks}
        students.append(student)
        print("Student added successfully.\n")
    except ValueError:
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
    
    