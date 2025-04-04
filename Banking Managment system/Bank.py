from database import *
from emp import *
import datetime
import random



class Bank:
    name = "Cash Hub Bank"
    address = "Dilsukhnagar Hyderabad"
    contact = "+91 9876543210"
    ifsc_code = "CHBNO300734"
    __password = "HUB.3007"


    @classmethod
    def change_password(cls):
        try:
            idno = int(input("Enter Identification Number"))
            if dbqueryone(f"SELECT STATUS FROM EMP WHERE EMPLOYEE_ID = {idno} "):
                e_password = input("Enter your password: ")
                if e_password == dbqueryone(f"SELECT PASSWORD FROM EMP WHERE EMPLOYEE_ID = {idno} "):
                    b_password = input("Enter Bank Password : ")
                    if b_password == cls.__password:
                        new_password = input("Enter your new password: ")
                        cls.__password = new_password
                        ename = dbqueryone(f"SELECT ENAME FROM EMP WHERE EMPLOYEE_ID = {idno}")
                        time = datetime.datetime.today().strftime("%Y-%m-%d %H:%M")
                        while True:
                            transaction_id = random.randint(100000,999999)
                            if transaction_id in ( dbquery(f"SELECT TRANSACTION_ID FROM BANKTRANS WHERE TRANSACTION_ID = {transaction_id}") ,dbquery(f"SELECT TRANSACTION_ID FROM CUSTTRANS WHERE TRANSACTION_ID = {transaction_id}")):
                                continue
                            else:
                                Bank.bank_transaction(transaction_id,idno,ename,"Password Change",time)
                                break
                        print("Password changed successfully!")
                    else:
                        print("Incorrect password!")
                else:
                    print("Incorrect password!")
            else:
                print("Invalid Identification Number")

        except:
            inp = input("Invalid Identification Number!\n(1) To Try A gain\n(2) To Exit")
            if inp == "1":
                cls.change_password()
            elif inp == "2":
                print("Exiting... Thankyou!")
            else:
                print("Enter Valid option")
        
    @classmethod
    def b_details(cls):
        print(f"Bank Name: {cls.name}")
        print(f"Address: {cls.address}")
        print(f"Contact: {cls.contact}")
        print(f"IFSC Code: {cls.ifsc_code}")
    
    @classmethod
    def change_bank_contact(cls):
        try:
            idno = int(input("Enter Identification Number"))
            if dbqueryone(f"SELECT STATUS FROM EMP WHERE EMPLOYEE_ID = {idno} "):
                e_password = input("Enter your password: ")
                if e_password == dbqueryone(f"SELECT PASSWORD FROM EMP WHERE EMPLOYEE_ID = {idno} "):
                    b_password = input("Enter Bank Password : ")
                    if b_password == cls.__password:
                        try:
                            new_contact_num = int(input("Enter your new Contact Number: +91 "))
                            if len(str(new_contact_num))!=10 and str(new_contact_num)[0] not in ["1", "2", "3", "4", "5","0"]:
                                print("Enter a Valid Contact Number")
                            else:
                                if new_contact_num == cls.contact_number:
                                    print("Contact Number Cannot Be Same")
                                else:
                                    cls.contact_number = new_contact_num
                                    ename = dbqueryone(f"SELECT ENAME FROM EMP WHERE EMPLOYEE_ID = {idno}")
                                    time = datetime.datetime.today().strftime("%Y-%m-%d %H:%M")
                                    while True:
                                        transaction_id = random.randint(100000,999999)
                                        if transaction_id in ( dbquery(f"SELECT TRANSACTION_ID FROM BANKTRANS WHERE TRANSACTION_ID = {transaction_id}") ,dbquery(f"SELECT TRANSACTION_ID FROM CUSTTRANS WHERE TRANSACTION_ID = {transaction_id}")):
                                            continue
                                        else:
                                            Bank.bank_transaction(transaction_id,idno,ename,"Contact Number Change",time)
                                            print("Contact Number changed successfully!")   
                                            break
                                            
                        except ValueError:
                            print("Please Enter a valid Contact Number")
                    else:
                        print("Incorrect password!")
                else:
                    print("Invalid Password")
            else:
                print("Invalid Identification Number")

        except:
            inp = ("Invalid Identification Number!\n(1) To Try A gain\n(2) To Exit")
            if inp == "1":
                cls.change_bank_contact()
            elif inp == "2":
                print("Exiting... Thankyou!")
            else:
                print("Enter Valid option")
    
    @staticmethod
    def bank_transaction(transaction_id,employee_id, ename,type,datetime):
        dbquery(f"INSERT INTO  BANKTRANS VALUES ({transaction_id}, {employee_id}, '{ename}','{type}',  '{datetime}')")
        mydb.commit()
    
    def check_bank_mods():
        try:
            idno = int(input("Enter Identification Number"))
            if dbqueryone(f"SELECT STATUS FROM EMP WHERE EMPLOYEE_ID = {idno} "):
                if dbqueryone(f"SELECT EMPLOYEE_ID FROM EMP WHERE JOB = 'MANAGER' "):
                    e_password = input("Enter your password: ")
                    if e_password == dbqueryone(f"SELECT PASSWORD FROM EMP WHERE EMPLOYEE_ID = {idno} "):
                        b_password = input("Enter Bank Password : ")
                        if b_password == Bank.__password:
                            print("Transaction History:")
                            print(f"Transaction ID\t\tEmployee_Id\t\tType\t\tDate Time")
                            for row in dbquery(f"SELECT * FROM BANKTRANS ORDER BY DATE_TIME DESC"):
                                print(f"{str(row[0]).center(14," ")}{row[1].center(25," ")}\t{str(row[3]).center(8," ")}\t{row[4]}")
                        else:
                            print("Incorrect Bank password!")
                    else:
                        print("Incorrect password!")
                else:
                    print("You are not a Manager!")
            else:
                print("Invalid Identification Number")
        except:
            print("Invalid Identification Number!")
