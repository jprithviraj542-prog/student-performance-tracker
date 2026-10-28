import json
import os

FILE = "students.json"
SUBJECTS = ["Maths", "Python", "SQL"]
students = []

def load_students():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            students.extend(json.load(f))

def save_students():
    with open(FILE, "w") as f:
        json.dump(students, f, indent=4)

def find_student(roll):
    for s in students:
        if s["roll"] == roll:
            return s
    return None

def get_number(message, low, high):
    while True:
        try:
            value = float(input(message))
            if low <= value <= high:
                return value
            print("Enter a number between", low, "and", high)
        except ValueError:
            print("Please enter a valid number")

def average(student):
    return sum(student["marks"].values()) / len(student["marks"])

def get_grade(avg):
    if avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "Fail"

def add_student():
    roll = input("Enter roll number: ")
    if find_student(roll):
        print("This roll number already exists!")
        return
    name = input("Enter student name: ")
    marks = {}
    for sub in SUBJECTS:
        marks[sub] = get_number(sub + " marks (0-100): ", 0, 100)
    attendance = get_number("Attendance % (0-100): ", 0, 100)
    students.append({"roll": roll, "name": name,
                     "marks": marks, "attendance": attendance})
    save_students()
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students yet.")
        return
    print("\nRoll | Name | Average | Grade | Attendance")
    for s in students:
        avg = average(s)
        print(s["roll"], "|", s["name"], "|", round(avg, 1), "|",
              get_grade(avg), "|", s["attendance"], "%")

def view_report():
    s = find_student(input("Enter roll number: "))
    if s is None:
        print("Student not found.")
        return
    print("\n--- Report Card ---")
    print("Name:", s["name"])
    for sub, mark in s["marks"].items():
        print(sub, ":", mark)
    avg = average(s)
    print("Average:", round(avg, 1))
    print("Grade:", get_grade(avg))
    print("Attendance:", s["attendance"], "%")
    if s["attendance"] < 75:
        print("WARNING: Low attendance!")

def update_marks():
    s = find_student(input("Enter roll number: "))
    if s is None:
        print("Student not found.")
        return
    for sub in SUBJECTS:
        s["marks"][sub] = get_number("New " + sub + " marks: ", 0, 100)
    save_students()
    print("Marks updated!")

def show_topper():
    if not students:
        print("No students yet.")
        return
    best = max(students, key=average)
    print("Topper:", best["name"], "with average", round(average(best), 1))

def delete_student():
    s = find_student(input("Enter roll number to delete: "))
    if s is None:
        print("Student not found.")
    else:
        students.remove(s)
        save_students()
        print("Student deleted!")

load_students()

while True:
    print("\n--- Student Analyzer ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. View Report Card")
    print("4. Update Marks")
    print("5. Show Topper")
    print("6. Delete Student")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        view_report()
    elif choice == "4":
        update_marks()
    elif choice == "5":
        show_topper()
    elif choice == "6":
        delete_student()
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
        