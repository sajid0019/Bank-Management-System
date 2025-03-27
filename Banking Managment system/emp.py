from database import *
import re
import random
class Emp:
    def create_employee():
        try:
            idno = int(input("Enter your Identification Number : "))
            if dbqueryone(f"SELECT EMPLOYEE_ID FROM EMP WHERE JOB = 'MANAGER' ") == idno:
                password = input("Enter your Password : ")
                if password == dbqueryone(f"SELECT PASSWORD FROM EMP WHERE EMPLOYEE_ID = {idno} "):
                    while True:
                        empid = random.randint(10000000, 99999999)
                        if dbqueryone(f"SELECT EMPLOYEE_ID FROM EMP WHERE EMPLOYEE_ID = {empid}"):
                            continue
                        else:
                            job = input("Enter position of the Employee : ")
                            ename = input("Enter name of the Employee : ")
                            age = int(input("Enter age of the Employee : "))
                            if 18<=age<=60:
                                place = input("Enter Address of Employee :")
                                try:
                                    phone = input("Enter Phone Number of Employee :")
                                    if len(str(phone)) ==10 and str(phone)[0] in ("6","7"):
                                        password = input("Enter  Password of Employee :")
                                        email = input("Enter Email of Employee :")
                                        if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
                                            while True:
                                                empid = random.randint(10000000, 99999999)
                                                if dbquery(f"SELECT EMPLOYEE_ID FROM EMP WHERE EMPLOYEE_ID = {empid}"):
                                                    continue
                                            else:
                                                dbquery(f"INSETR INTO EMP VALUES ({empid},'{name}',{age},'{address}',{phone},'{email}','{job}','{password}',True)")
                                        else:
                                            print("Invalid Email")
                                    else:
                                        print("Invalid Phone Number")
                                except Exception:
                                    print("Invalid Phone Number")             
                            else:
                                print("Employee Should be 18+")                            
                else:
                    print("Invalid Password")
                    print()
            else:
                print("You are not a Manager!")
                print()
        except:
            print("Enter a valid Identification Number")
            print()

        def e_display():
            try:
                idno = int(input("Enter your Identification Number :"))
                if  dbqueryone(f"SELECT EMPLOYEE_ID FROM EMP WHERE EMPLOYEE_ID = {idno};"):
                    if  dbqueryone(f"SELECT STATUS FROM EMP WHERE EMPLOYEE_ID = {idno};"):
                        password = input("Enter your Password :")
                        if password == dbqueryone(f"SELECT PASSWORD FROM EMP WHERE EMPLOYEE_ID = {idno};"):
                            print(f"""Name: {dbqueryone(f"SELECT ename FROM EMP WHERE EMPLOYEE_ID = {idno};")}""")
                            print(f"""Age: {dbqueryone(f"SELECT AGE FROM EMP WHERE EMPLOYEE_ID = {idno};")}""")
                            print(f"""Phone: {dbqueryone(f"SELECT PHONE FROM EMP WHERE EMPLOYEE_ID = {idno};")}""")
                            print(f"""Email: {dbqueryone(f"SELECT EMAIL FRO EMP WHERE EMPLOYEE_ID = {idno};")}""")
                            print(f"""Address: {dbqueryone(f"SELECT ADDRESS FROM EMP WHERE EMPLOYEE_ID = {idno};")}""")
                        else:
                            print("Invalid Password")
                            print()
                    else:
                        print("Employee Not Found!")
                        print()
                else:
                    print("Invalid Identification Number!")
                    print()

            except :
                print("Enter a valid Identification Number")
                print()

    def change_number():
        try:
            idno = int(input("Enter your Identification Number :"))
            if  dbqueryone(f"SELECT EMPLOYEE_ID FROM EMP WHERE EMPLOYEE_ID = {idno};"):
                if  dbqueryone(f"SELECT STATUS FROM EMP WHERE EMPLOYEE_ID = {idno};"):
                    password = input("Enter your Password :")
                    if password == dbqueryone(f"SELECT PASSWORD FROM EMP WHERE EMPLOYEE_ID = {idno};"):
                        new_phone = int(input("Enter your new Contact Number :"))
                        if len(str(new_phone))!=10 and str(new_phone)[0] not in ["1", "2", "3", "4", "5","0"]:
                            print("Enter a Valid Contact Number")
                        else:
                            if new_phone == dbqueryone(f"SELECT PHONE FROM EMP WHERE EMPLOYEE_ID = {idno};"):
                                print("Contact Number Cannot Be Same")
                            else:
                                dbqueryone(f"UPDATE EMP SET PHONE = {new_phone} WHERE EMPLOYEE_ID = {idno};")
                                print("Contact Number Changed Successfully")
                    else:
                        print("Invalid Password")
                        print()
                else:
                    print("Employee Not Found!")
                    print()
            else:
                print("Invalid Identification Number!")
                print()
        except :
            print("Enter a valid Identification Number")
            print()

    def change_email():
        try:
            idno = int(input("Enter your Identification Number :"))
            if  dbqueryone(f"SELECT EMPLOYEE_ID FROM EMP WHERE EMPLOYEE_ID = {idno};"):
                if  dbqueryone(f"SELECT STATUS FROM EMP WHERE EMPLOYEE_ID = {idno};"):
                    password = input("Enter your Password :")
                    if password == dbqueryone(f"SELECT PASSWORD FROM EMP WHERE EMPLOYEE_ID = {idno};"):
                        new_email = input("Enter your new Email :")
                        if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', new_email):
                            if new_email == dbqueryone(f"SELECT EMAIL FROM EMP WHERE EMPLOYEE_ID = {idno};"):
                                print("Email Cannot be the same as the old one")
                            else:
                                dbqueryone(f"UPDATE EMP SET EMAIL = '{new_email}' WHERE EMPLOYEE_ID = {idno};")
                                print("Email Changed Successfully")
                        else:
                            print("Enter a Valid Email")
                    else:
                        print("Invalid Password")
                        print()
                else:
                    print("Employee Not Found!")
                    print()
            else:
                print("Invalid Identification Number!")
                print()        
        except :
            print("Enter a valid Identification Number")
            print()
        
    def change_password():
        try:
            idno = int(input("Enter your Identification Number :"))
            if  dbqueryone(f"SELECT EMPLOYEE_ID FROM EMP WHERE EMPLOYEE_ID = {idno};"):
                if  dbqueryone(f"SELECT STATUS FROM EMP WHERE EMPLOYEE_ID = {idno};"):
                    password = input("Enter your Password :")
                    if password == dbqueryone(f"SELECT PASSWORD FROM EMP WHERE EMPLOYEE_ID = {idno};"):
                        new_password = input("Enter your new Password :")
                        if new_password == password:
                            print("Password cannot be the same as the old one")
                        else:
                            dbqueryone(f"UPDATE EMP SET PASSWORD = '{new_password}' WHERE EMPLOYEE_ID = {idno};")
                            print("Password Changed Successfully")
                    else:
                        print("Invalid Password")
                        print()
                else:
                    print("Employee Not Found!")
                    print()
            else:
                print("Invalid Identification Number!")
                print()
        except :
            print("Enter a valid Identification Number")
            print()