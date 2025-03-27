
from database import*
from customer import *
from Bank import *


def operation():
        while True :
            print("🏦💰Wellcome To Cash Hub Bank💰🏦")
            func = input("(1) Customer services\n(2) Bank services\n(3) Employee services\n(4) Exit.....  :")
            print()
            if  func == "1":
                inp = input("(1) Cash deposit/withdrawl\n(2) Password Change\n(3) Phone Number Update\n(4) Display your details\n(5) Display Bank details\n(6) Create New Bank Account\n(7) Delete Bank Account  :")
                print()
                if  inp =="1":
                    Customer.cash()
                    print()
                elif    inp=="2":
                    Customer.change_password()
                    print()
                elif    inp=="3":
                    Customer.changecustcontact()
                    print()
                elif    inp=="4":
                    Customer.c_display()
                    print()
                elif    inp=="5":
                    Bank.b_details()
                    print()
                elif    inp=="6":
                    Customer.create_account()
                    print()
                elif    inp=="7":
                    Customer.delete_account()
                    print()
                else:
                    print("Invalid Input ")
                
            elif    func=="2":
                inp = input("(1) Display Bank details\n(2) Change Bank Password\n(3) Change Bank Contact Number\n(4) Register Bank Employee\n(5) Check Bank Modifications :")
                print()
                if  inp == "1":
                    Bank.b_details()
                    print()
                elif    inp=="2":
                    Bank.change_password()
                    print()
                elif    inp=="3":
                    Bank.change_bank_contact()
                    print()
                elif    inp=="4":
                    Emp.create_employee()
                    print()
                elif    inp=="5":
                    Bank.check_bank_mods()
                    print()
                else:
                    print("Invalid Input")
            elif    func == "3":
                inp = input("(1) Contact Number Update\n(2) Email Update\n(3) Password Change\n(4) Display your details\n(5) Display Bank details")
                print()
                if  inp =="1":
                    Emp.change_number()
                    print()
                elif    inp=="2":
                    Emp.change_email()
                    print()
                elif    inp=="3":
                    Emp.change_password()
                    print()
                elif    inp=="4":
                    Emp.e_display()
                    print()
                elif    inp=="5":
                    Bank.b_details()
                    print() 
                else:
                    print("Invalid Input")

            else:
                print("Invalid Input")
                print()

operation()
