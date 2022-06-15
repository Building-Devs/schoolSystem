database = {
    # "student_ID" : "student_name"

    "102006": "Clinton Woods",
    "102004": "John Fritz",
    "102003": "Jenny Clarkson",
    "102001": "Makaila Rodriguez",
    "102002": "Rebecca Page",
    "102005": "Luis Alvarez"
}

# ---Response---
prompt = input("Welcome to  Jenny Montessori student Database Management System. Please choose an option:\n"
               "1. Check if your name is in the school's database\n"
               "2. Add a student's name and ID to the database\n"
               "3. Update or Change details of an existing student in the database\n\n"
               "Enter you response: ")


def response():

# option 1
    if prompt == "1":
        key = database.keys()
        s_id = input("\nEnter valid Student ID: ")
        if s_id in key:
            print(f"\nName: {database.get(s_id)}")
            exit()
        elif s_id != key:
            print(f"\nError! Student ID does not match a name.")
            exit()

# option 2
    elif prompt == "2":
        s_id = input("\nEnter new unique Student ID: ")
        s_name = input("Enter Student name: ")
        new_student = {s_id: s_name}
        database.update(new_student)
        key = database.keys()
        verify = input("\nDetails have been added to the database successfully. Would you like to verify? (Yes/No): ")
        if verify.lower() == "yes":
            s_id = input("\nRe-enter new unique Student ID: ")
            if s_id in key:
                print(f"\nName: {database.get(s_id)}\n")
                print(f"_____Updated database_____")

                # print keys and values in updated database side by side.
                for (key, values) in database.items():
                    print(f"{key} - {values}")
            else:
                print(f"Error! Student ID does not match a name")
        elif verify.lower() == "no":
            exit()

# option 3/
    elif prompt == "3":
        s_id = input("Enter Student ID: ")
        s_name = input("Enter new Student name: ")
        update_ = {s_id: s_name}
        database.update(update_)
        key = database.keys()
        verify = input("\nUpdate Complete. Would you like to verify? (Yes/No): ")
        if verify.lower() == "yes":
            s_id = input("\nRe-enter Student ID: ")
            if s_id in key:
                print(f"\nName: {update_.get(s_id)}\n")
                print(f"_____Updated database_____")
                for (key, values) in database.items():
                    print(f"{key} - {values}")
            else:
                print(f"Error! Student ID does not match a name.")
        elif verify.lower() == "no":
            exit()

# invalid option
    else:
        print("Invalid response.-")


response()


# Group 1 : Aaron and Antoine
