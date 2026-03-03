import json
import os

class Student:
    def __init__(self, roll, name, age):
        self.roll = roll
        self.name = name
        self.age = age

    def to_dict(self):
        return {
            "roll": self.roll,
            "name": self.name,
            "age": self.age
        }


class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        return []

    def save_data(self):
        with open(self.filename, "w") as file:
            json.dump(self.students, file, indent=4)

    def add_student(self):
        try:
            roll = int(input("Enter Roll Number: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))

            student = Student(roll, name, age)
            self.students.append(student.to_dict())
            self.save_data()

            print("✅ Student Added Successfully!\n")
        except ValueError:
            print("❌ Invalid input!\n")

    def view_students(self):
        if not self.students:
            print("No students found.\n")
            return

        print("\n--- Student List ---")
        for s in self.students:
            print(f"Roll: {s['roll']} | Name: {s['name']} | Age: {s['age']}")
        print()

    def search_student(self):
        roll = int(input("Enter Roll Number to Search: "))
        for s in self.students:
            if s["roll"] == roll:
                print(f"Found: {s}")
                return
        print("❌ Student Not Found\n")

    def delete_student(self):
        roll = int(input("Enter Roll Number to Delete: "))
        for s in self.students:
            if s["roll"] == roll:
                self.students.remove(s)
                self.save_data()
                print("🗑 Student Deleted\n")
                return
        print("❌ Student Not Found\n")


def main():
    manager = StudentManager()

    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.view_students()
        elif choice == "3":
            manager.search_student()
        elif choice == "4":
            manager.delete_student()
        elif choice == "5":
            print("Exiting Program...")
            break
        else:
            print("❌ Invalid Choice\n")


if __name__ == "__main__":
    main()