import curd   # IMPORTED MODULE NAMES AS CURD 


# ---------- SHOWS ALL STUDENTS NAME AND MARKS ----------
def view_all_students():
    students_data = curd.load_students()

    if not students_data:
        print("students data not available")
    curd.show_students(students_data)


FILE = "student.txt"  # THIS IS FILE WHICH STORES ALL DATA OF STUDENT



# ---------- APP STARTS FROM HERE ----------
def main():
    print("\n------ STUDENT MANAGER APP -------")
    while True:
        print("\n1.Add Student. \n2.View all students. \n3.View Class Analytics. \n4.Update name of student. \n5.Update marks of student. \n6.Remove student. \n7.View Report-Card of student.\n8.View topper. \n9.Exit. ")

        
        choice = input("Enter student's marks(1-9): ")
        if not choice.isdigit() or not (1 <= int(choice) <= 9):
            print("Invalid choice!..")
            exit

        choice = int(choice)
            
        if choice == 1:
            curd.add_student()
        elif choice == 2:
            view_all_students()
        elif choice == 3:
            curd.class_analytics()
        elif choice == 4:
            curd.update_student_name()
        elif choice == 5:
            curd.update_student_mark()
        elif choice == 6:
            curd.remove_student()
        elif choice == 7:
            curd.report_card_of_student()
        elif choice == 8:
            curd.find_topper()
        elif choice == 9:
            print("\nExiting......")
            break
        else:
            print("Invalid input!...")



# ---------- APP RUNS HERE ----------
if __name__ == "__main__":
    main()