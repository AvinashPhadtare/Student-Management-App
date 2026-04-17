FILE = "student.txt"



# ---------- ADD NEW STUDENT WITH MARKS ----------
def add_student():
    name = input("Enter student name: ")
    if not name.strip():
        print("Name cannot be empty")
        return
    
    marks = input("Enter student's marks(1-100): ")
    if not marks.isdigit() or not (1 <= int(marks) <= 100):
        print("Invalid marks!..")
        return

    marks = int(marks)

    try:
        with open(FILE, "r") as f:  
            for line in f:
                stored_student_name = line.strip().split(":")[0]
                if name.lower() == stored_student_name.lower():
                    print("Student already exists")
                    return
    except FileNotFoundError:
        pass

    with open(FILE, "a") as f:
        f.write(f"{name}:{marks}\n")

    print("Student added successfully")



# ---------- REMOVE STUDENT ----------
def remove_student():
    name = input("Enter name of student to remove: ").strip()
    if not name.strip():
        print("Name cannot be empty")
        return

    try:
        with open(FILE, "r") as f:
            data = f.readlines()
    except FileNotFoundError:
        print("File not found")
        return

    updated_data = []
    found = False

    for line in data:
        student_name, marks = line.strip().split(":")

        if student_name.lower() == name.lower():
            found = True
            continue  # skip this line (delete)
        else:
            updated_data.append(line)

    if not found:
        print("Student not found in file")
    else:
        with open(FILE, "w") as f:
            f.writelines(updated_data)
        print("Student deleted successfully")



# ---------- UPDATE STUDENT NAME ----------
def update_student_name():
    old_name = input("Enter Current name: ").strip()
    if not old_name.strip():
        print("Name cannot be empty")
        return
    new_name = input("Enter new name: ")
    if not new_name.strip():
        print("Name cannot be empty")
        return
    
    try:
        with open(FILE, 'r') as f:
            data = f.readlines()
    except FileNotFoundError:
        print("File not found")
        return
    
    for line in data:
        existing_name = line.strip().split(":")[0]
        if existing_name.lower() == new_name.lower():
            print("New name is already exists")
            return

    updated_data = []
    found = False

    for line in data:
        name, marks = line.strip().split(":")
        if name.lower() == old_name.lower():
            new_line = f"{new_name}:{marks}\n"
            found = True
        else:
            new_line = line

        updated_data.append(new_line)

    if not found:
        print("This name does not exists!.. ")
    else:
        with open(FILE, "w") as f:
            f.writelines(updated_data)
        print("Student name updated successfully")



# ---------- UPDATE STUDENT MARKS ----------
def update_student_mark():
    old_name = input("Enter name of student which you want to update marks of: ").strip()
    if not old_name.strip():
        print("Name cannot be empty")
        return
    new_marks = input("Enter new marks: ")

    if not new_marks.isdigit() or not (1 <= int(new_marks) <= 100):
        print("Invalid input")
        return
    
    else:
        try:
            with open(FILE, 'r') as f:
                data = f.readlines()
        except FileNotFoundError:
            print("File not found")
            return
        
        updated_data = []
        found = False

        for line in data:
            name, marks = line.strip().split(":")
            if name.lower() == old_name.lower():
                new_line = f"{name}:{new_marks}\n"
                found = True
            else:
                new_line = line

            updated_data.append(new_line)

        if not found:
            print("This name does not exists!.. ")
        else:
            with open(FILE, "w") as f:
                f.writelines(updated_data)
            print("Student marks updated successfully")



# ---------- LOAD STUDENTS DETAILS ----------
def load_students():
    student_dict = {}

    try:
        with open(FILE, "r") as f:
            for line in f:
                if ":" in line:
                    name, mark = line.strip().split(":")
                    student_dict[name.lower()] = int(mark)
    except FileNotFoundError:
        print("Student's details file not found")

    return student_dict



# ---------- SHOW STUDENT DETAILS ----------
def show_students(details):
    if not details:
        print("File of students is empty")
        return

    print("\n----- Details -----")

    for i, (name, marks) in enumerate(details.items(), 1):
        print(f"{i}. {name.capitalize():<10} : {marks}")



# ---------- SHOW TOPPER ----------
def find_topper():
    try:
        with open(FILE, "r") as f:
            data = f.readlines()
    except FileNotFoundError:
        print("File not found")
        return

    if not data:
        print("No student data available")
        return

    topper_name = ""
    topper_marks = -1

    for line in data:
        if ":" in line:
            name, marks = line.strip().split(":")
            marks = int(marks)

            if marks > topper_marks:
                topper_marks = marks
                topper_name = name


    if topper_name == "":
        print("No valid student records found")
    else:
        print(f"\n** -- Topper is {topper_name.capitalize()} with {topper_marks} marks -- **")



# ---------- COUNT ALL STUDENTS ----------
def count_students():
    students = load_students()
    count = len(students)
    if count:
        return count
    else:
        raise Exception("No Student exists in file")
    


# ---------- COUNT ALL PASSED OR FAILED STUDENTS ----------
def pass_fail_count():
    pass_count = 0
    fail_count = 0

    try:
        with open(FILE, 'r') as f:
            data = f.readlines()
    except FileNotFoundError:
        print("File not found")
        return
    
    for line in data:
        student_name, marks = line.strip().split(":")
        marks = int(marks)
        if 45 <= marks <= 100:
            pass_count += 1
        else:
            fail_count += 1

    return pass_count,fail_count



# ---------- SHOWS REPORT CARD OF STUDENT ----------
def report_card_of_student():
    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty")
        return
     
    try:
        with open(FILE, 'r') as f:
            data = f.readlines()
    except FileNotFoundError:
        print("File not found")
        return

    found = False

    for line in data:
        student_name, marks = line.strip().split(":")

        if student_name.lower() == name.lower():
            marks = int(marks)
            found = True
            
            if 45 <= marks <= 100:
                print(f"\n-------- Report Card --------\nStudent name: {student_name.capitalize()}\nStudent marks: {marks}\nStudent status: {student_name.capitalize()} is Passed")
            else:
                print(f"\n-------- Report Card --------\nStudent name: {student_name.capitalize()}\nStudent marks: {marks}\nStudent status: {student_name.capitalize()} is Failed")
            break

    if not found:
        print("Student not found")



# ---------- SHOWS CLASS ANALYTICS ----------
def class_analytics():
    total_marks = 0
    try:
        with open(FILE, 'r') as f:
            data = f.readlines()
    except FileNotFoundError:
        print("File not found")
        return
    
    for line in data:
        student_name, student_marks = line.strip().split(":")
        total_marks += int(student_marks)

      
    student_count = count_students()
    if student_count == 0:
        print("Student's not exists in file")
        return
    else:
        average = total_marks/student_count

    Pass_count,Fail_count = pass_fail_count()

    pass_percentage = (Pass_count/student_count) * 100
    
    print("\n-------- Class Analytics --------\n")
    print(f"1.Average of Class is: {average}\n2.Class Pass Percentage: {pass_percentage}\n3.Total Student Passed: {Pass_count}\n4.Total Student Failed: {Fail_count}")
    

