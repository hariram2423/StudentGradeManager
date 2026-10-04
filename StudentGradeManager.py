students = {}


def get_mark(subject):
    while True:
        try:
            mark = float(input(f"Enter {subject} mark (0-100): "))

            if 0 <= mark <= 100:
                return mark
            else:
                print("Invalid mark! Please enter a value between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter a number.")


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def add_student():
    name = input("Enter student name: ")

    math = get_mark("Math")
    science = get_mark("Science")
    english = get_mark("English")

    average = (math + science + english) / 3
    grade = calculate_grade(average)

    students[name] = {
        "Math": math,
        "Science": science,
        "English": english,
        "Average": average,
        "Grade": grade
    }

    print(f"\nStudent {name} added successfully!")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")


def display_students():
    if not students:
        print("\nNo students found.")
        return

    print("\n--- Student Grade Report ---")

    for name, details in students.items():
        print(f"\nName: {name}")
        print(f"Math: {details['Math']}")
        print(f"Science: {details['Science']}")
        print(f"English: {details['English']}")
        print(f"Average: {details['Average']:.2f}")
        print(f"Grade: {details['Grade']}")


while True:
    print("\n===== Student Grade Manager =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        print("Program ended.")
        break

    else:
        print("Invalid choice. Please try again.")