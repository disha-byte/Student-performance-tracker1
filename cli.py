# cli.py
from services import (
    init_db, add_student, add_grade, get_student_details, calculate_average,
    list_students, subject_topper, class_average, export_backup_json, export_backup_csv
)

def print_menu():
    print("\n=== Student Performance Tracker (CLI) ===")
    print("1. Add Student")
    print("2. Add / Update Grade")
    print("3. View Student Details")
    print("4. Calculate Student Average")
    print("5. List All Students")
    print("6. Subject-wise Topper")
    print("7. Class Average by Subject")
    print("8. Export Backup (JSON & CSV)")
    print("9. Exit")

def main():
    init_db()
    while True:
        print_menu()
        choice = input("Choose an option (1-9): ").strip()

        if choice == '1':
            name = input("Enter student name: ").strip()
            roll = input("Enter roll number: ").strip()
            cls  = input("Class (optional): ").strip()
            ok, msg = add_student(roll, name, cls if cls else None)
            print(msg)

        elif choice == '2':
            roll = input("Enter roll number: ").strip()
            subject = input("Subject (e.g., Math, Science, English): ").strip()
            try:
                score = float(input("Score (0-100): ").strip())
            except ValueError:
                print("Invalid score.")
                continue
            ok, msg = add_grade(roll, subject, score)
            print(msg)

        elif choice == '3':
            roll = input("Enter roll number: ").strip()
            student, grades = get_student_details(roll)
            if not student:
                print("Student not found.")
            else:
                print(f"\nName: {student['name']} | Roll: {student['roll']} | Class: {student['class_name']}")
                print("Grades:")
                if grades:
                    for sub, sc in grades:
                        print(f" - {sub}: {sc}")
                else:
                    print(" (no grades yet)")
                avg = calculate_average(roll)
                print(f"Average: {avg if avg is not None else 'N/A'}")

        elif choice == '4':
            roll = input("Enter roll number: ").strip()
            avg = calculate_average(roll)
            if avg is None:
                print("Student not found or no grades.")
            else:
                print(f"Average for {roll}: {avg:.2f}")

        elif choice == '5':
            students = list_students()
            if not students:
                print("No students yet.")
            else:
                for s in students:
                    print(f"{s['roll']} - {s['name']} ({s['class_name']})")

        elif choice == '6':
            sub = input("Enter subject: ").strip()
            toppers = subject_topper(sub)
            if not toppers:
                print("No data for this subject.")
            else:
                top = toppers[0][2]
                print(f"Top score in {sub}: {top}")
                for r, n, sc in toppers:
                    print(f" - {n} (Roll {r}) : {sc}")

        elif choice == '7':
            avgs = class_average()
            if not avgs:
                print("No grades yet.")
            else:
                for sub, avg in avgs:
                    print(f"{sub}: {avg}")

        elif choice == '8':
            j = export_backup_json()
            c = export_backup_csv()
            print(f"Exported:\n  JSON → {j}\n  CSV  → {c}")

        elif choice == '9':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
