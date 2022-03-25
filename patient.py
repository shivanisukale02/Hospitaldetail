import sqlite3
con = sqlite3.connect('hospital.db')
cursor = con.cursor()
#sqlite_query = '''CREATE TABLE Patient_detail(patientCode INTEGER PRIMARY KEY, name TEXT NOT NULL,
#address TEXT Not NULL, phone TEXT NOT NULL);'''
#cursor.execute(sqlite_query)
#print('table is created successfully')

def Add_Patient_details():  # add patient details
    Patient_Code = input("Enter Patient Code : ")
    Name = input("Enter Patient Name : ")
    Address=input("Enter Patients Address")
    Phone_no = input("Enter Patients phone no. : ")
    data = (Patient_Code, Name, Address, Phone_no)
    insert_query = '''INSERT INTO Patient_detail VALUES (?,?,?,?)'''
    cursor.execute(insert_query, data)
    con.commit()
    print("Patient Added Successfully\n ")
    main1()


def Display_Patients():  # display patients details
    sqlite_select_query = '''SELECT * FROM Patient_detail'''
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    print(records)
    for row in records:
        print('Patient_Code: ', row[0])
        print('Name: ', row[1])
        print('Address :',row[2])
        print('Phone_No.: ', row[3])
        print("------------")
        # con.close()
    main1()


def main1():
    print("\n\nEnter below no to perform following operations ")
    print("To Add Patient enter1 ")
    print("To View All Patients enter2 ")
    print("To Exit enter3")
    ch = int(input("Enter your Choice "))
    if ch == 1:
        Add_Patient_details()
    elif ch == 2:
        Display_Patients()
    elif ch == 3:
        exit(0)

    else:
        print("Invalid Choice")
        main1()

main1()