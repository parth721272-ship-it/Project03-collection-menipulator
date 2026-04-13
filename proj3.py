# Student ni mahiti store karva mate list banavi
students = []

# (program chalu rakhva mate loop ne use karvu)
while True:
    # menu batavvu
    print("\nWelcome to the Student Data Organizer!")
    print("1. Add Student")  
    print("2. Display All Students")  
    print("3. Update Student Information")
    print("4. Delete Student") 
    print("5. Display Subjects Offered") 
    print("6. Exit")

    # user pase thi choice laine option btva mate
    option = input("Enter your choice: ")

    # 1)student add karva mate
    if option == '1':
        student_id = input("Student ID: ")
        name = input("Name: ")  
        age = int(input("Age: "))
        grade = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")  #(date of birth) ni format specify karva mate
        subjects_input = input("Subjects (comma-separated): ")  # subjects ni list comma thi alag karva mate

        # subjects ne set ma convert karvu (duplicate door karva)
        subjects = set(subject.strip() for subject in subjects_input.split(','))

        # ID ane DOB tuple ma store karvu
        id_dob = (student_id, dob)

        # student ni mahiti dictionary ma store karvi
        #ek dictionary chhe je student ni badhi detail rakhe chhe
        student_data = {
            "id_dob": id_dob,
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subjects
        }

        # list ma add karvu
        students.append({student_id: student_data})
        print("Student added successfully!") 

    # badha studentio batava mate
    elif option == '2':
        if not students:
            print("No student records found.")  # jo record na hoy
        else:
            # dairek student batavvo
            for record in students:
                for sid, info in record.items():
                    print(f"Student ID: {sid} | Name: {info['name']} | Age: {info['age']} | Grade: {info['grade']} | Subjects: {', '.join(info['subjects'])}")

    # student update karva mate
    elif option == '3':
        sid = input("Enter student ID to update: ")  # ID lakho
        found = False  # male chhe ke nahi check

        for record in students:
            if sid in record:
                info = record[sid]
                found = True

                # update menu
                print("1. Update Name")
                print("2. Update Age")
                print("3. Update Grade")
                print("4. Update Subjects")

                choice = input("Choose field to update: ")

                # choice pramane update
                if choice == '1':
                    info['name'] = input("Enter new name: ")
                elif choice == '2':
                    info['age'] = int(input("Enter new age: "))
                elif choice == '3':
                    info['grade'] = input("Enter new grade: ")
                elif choice == '4':
                    new_subjects = input("Enter new subjects (comma-separated): ")
                    info['subjects'] = set(sub.strip() for sub in new_subjects.split(','))

                print("Student info updated.")
                break

        if not found:
            print("Student ID not found.")  # jo na male

    # vidyarthi delete karva mate
    elif option == '4':
        sid = input("Enter student ID to delete: ")
        found = False

        for i, record in enumerate(students):
            if sid in record:
                del students[i]  # list mathi delete karvu
                print("Student record deleted.")
                found = True
                break

        if not found:
            print("Student ID not found.")

    # badha subjects batava mate
    elif option == '5':
        all_subjects = set()  # khali set

        for record in students:
            for data in record.values():
                all_subjects.update(data['subjects'])  # subjects add karva

        if all_subjects:
            print("Subjects Offered:", ", ".join(all_subjects))
        else:
            print("No subjects found.")

    # program bandh karva mate
    elif option == '6':
        print("Thank you for using the Student Data Organizer.")
        break  # loop bandh

    # invalid choice mate
    else:
        print("Invalid option. Try again.")