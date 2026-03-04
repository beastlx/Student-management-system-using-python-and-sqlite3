import sqlite3

# Connect
conn = sqlite3.connect("students.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


#CREATING THE TABLE STUDENTS
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fname TEXT,
    lname TEXT,
    age INTEGER,
    level TEXT,
    course TEXT,
    phone_no TEXT, 
    stud_id TEXT UNIQUE,
    date_reg TEXT
    )            
""")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. update a student's information")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
    # Adding students detatils into the table "students"
        fname= input("enter your first name ")
        lname= input("enter your last name ")
        age=int(input("enter your age "))
        level=input("enter your level ")
        course=input("enter your course ")
        phone_no= input("enter your phone number ")
        stud_id= input("enter your matric number ")
        date_reg=input("enter your date of registration ")
        cursor.execute("""
        INSERT  INTO students(fname,lname,age,level,course,phone_no,stud_id,date_reg)
        VALUES (?,?,?,?,?,?,?,?)""",(fname,lname,age,level,course,phone_no,stud_id,date_reg))
        conn.commit()
        print("Student added successfully.")

    elif choice == "2":
    # showing the students added into the database and their details
        cursor.execute("""SELECT * FROM students """)
        records= cursor.fetchall()
        for record in records:
            print(dict(record))


    elif choice == "3":
        #user input to find a specific student by matric number
        naze=input("enter the ID of the student your searching for ")
        cursor.execute("SELECT * FROM students WHERE stud_id = ?", (naze,))
        find=cursor.fetchone()
        if find:
            print(dict(find))
        else:
            print("Student not found.")


    elif choice == "4":
        #delete a particular student's record 
        delname= input("enter the ID of the student you want to delete ")
        cursor.execute("DELETE FROM students WHERE stud_id =? ",(delname,))
        print("Student's record removed successfully.")


        conn.commit()
    elif choice == "5":
        couse=input("enter the course you would like to change to ")
        nae=input("enter the ID of the student your searching for ")
        cursor.execute("UPDATE students SET course = ? WHERE stud_id= ? ",(couse,nae))
        conn.commit()
        print("course changed successfully.")

    elif choice =="6":

        
        break

conn.close()