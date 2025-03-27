from database import *
import random
import datetime
class Customer:
    def __init__(self, name, age, place, phone,password,account_num ):
        self.name = name
        self.age = age
        self.place = place
        self.phone = phone
        self.password = password
        self.account_num = account_num
        self.balance = 0

    
    def create_account(self):
        name = input("Enter your Name :")
        try:
            age = int(input("Enter your Age :"))
            if 18<=age<=60:
                place = input("Enter your Address :")
                try:
                    phone = input("Enter your Phone Number :")
                    if len(str(phone)) ==10 and str(phone)[0] in ("6","7"):
                        password = input("Enter your Password :")
                        while True:
                            account_num = random.randint(100000000000,999999999999)
                            acno = dbquery(f"SELECT ACCOUNT_NUM FROM CUSTOMER WHERE ACCOUNT_NUM = {account_num}") 
                            if acno:
                                continue
                            else:
                                dbquery(f"INSERT INTO CUSTOMER VALUES ('{self.name}', {self.age},{self.balance} ,'{self.place}', '{self.password}', {self.phone},{self.account_num},True)")
                                mydb.commit() 
                                break
                    else:
                        print("Invalid Phone Number")
                except Exception:
                    print("Invalid Phone Number")
                    
        except Exception:
            print("Invalid Input")
            print()
        
        
            
        
    
    def c_display():
        try:
            inp = int(input("Enter your Account Number :"))
            if  dbqueryone(f"SELECT ACCOUNT_NUM FROM CUSTOMER WHERE account_num = {inp};"):
                if  dbqueryone(f"SELECT STATUS FROM CUSTOMER WHERE account_num = {inp};"):
                    print(f"""Name: {dbqueryone(f"SELECT Username FROM CUSTOMER WHERE account_num = {inp};")}""")
                    print(f"""Age: {dbqueryone(f"SELECT AGE FROM CUSTOMER WHERE account_num = {inp};")}""")
                    print(f"""Phone: {dbqueryone(f"SELECT Phone FROM CUSTOMER WHERE account_num = {inp};")}""")
                    print(f"""BALANCE: {dbqueryone(f"SELECT BALANCE FROM CUSTOMER WHERE account_num = {inp};")}""")
                    print(f"""Address: {dbqueryone(f"SELECT PLACE FROM CUSTOMER WHERE account_num = {inp};")}""")
                    print("Your account Created Successfully")
                    print()
                else:
                    print("Invalid Account Number")
                    print()

            else:
                    print("Invalid Account Number")
                    print()
           
        except Exception:
             print("Enter a valid Account Number")
             print()


    def changecustpassword():
        try:
            if  dbqueryone(f"SELECT STATUS FROM CUSTOMER WHERE account_num = {inp};"):
                inp = int(input("Enter your Account Number :"))
                old_pass = input("Enter your old Password :")
                if old_pass == dbqueryone(f"SELECT Password FROM CUSTOMER WHERE account_num = {inp};"):
                    new_pass = input("Enter your new Password :")
                    dbquery(f"UPDATE CUSTOMER SET PASSWORD = '{new_pass}' WHERE account_num = {inp};")
                    print("Password Changed Successfully")
                    print()
                else:
                    print("Invalid Password")
                    print()

            else:
                print("Invalid Account Number")
                print()
        except :
            print("Enter a valid Account Number")
            print()

    def changecustcontact():
        try:
            inp = int(input("Enter your Account Number :"))
            if  dbqueryone(f"SELECT STATUS FROM CUSTOMER WHERE account_num = {inp};"):
                password = input("Enter your Password")
                if password == dbqueryone(f"SELECT PASSWORD FROM CUSTOMER WHERE account_num ={inp}"):
                    try:
                        new_phone = int(input("Enter your new Phone Number : +91 "))
                        if len(str(new_phone)) == 10:
                            if str(new_phone)[0] not  in ("6","7","8","9"):
                                print("Phone Number is invalid")
                            else:
                                dbquery(f"UPDATE CUSTOMER SET Phone = {new_phone} WHERE account_num = {inp};")
                                print("Phone Number Changed Successfully")
                                print()
                        else:
                            print("Invalid Phone Number")
                            print()
                    except:
                        print("Enter a valid Phone Number")
                        print()
                else:
                    print("Invalid Password")
                    print()
            else:
                print("Invalid Account Number")
                print()
        except :
            print("Enter a valid Account Number")
            print()

 

    def w_cash():
        try:
            inp = int(input("Enter your Account Number :"))
            if  dbqueryone(f"SELECT STATUS FROM CUSTOMER WHERE account_num = {inp};"):
                password = input("Enter your Password")
                if password == dbqueryone(f"SELECT PASSWORD FROM CUSTOMER WHERE account_num ={inp}"):
                    try:
                        w_amount = float(input("Enter the Withdraw Amount :"))
                        if w_amount <= dbqueryone(f"SELECT BALANCE FROM CUSTOMER WHERE account_num ={inp}"):
                            balance = dbqueryone(f"SELECT BALANCE FROM CUSTOMER WHERE account_num ={inp}") - w_amount
                            dbquery(f"UPDATE CUSTOMER SET BALANCE = {balance} WHERE account_num = {inp};")
                            print("Withdrawal Successful")
                            time = datetime.datetime.today().strftime("%Y-%m-%d %H:%M")
                            print()
                            while True:
                                transaction_id = random.randint(100000,999999)
                                if transaction_id in ( dbquery(f"SELECT TRANSACTION_ID FROM BANKTRANS WHERE TRANSACTION_ID = {transaction_id}") ,dbquery(f"SELECT TRANSACTION_ID FROM CUSTTRANS WHERE TRANSACTION_ID = {transaction_id}")):
                                    continue
                                else:
                                    Customer.create_transaction(transaction_id,inp,"Withdrawl",w_amount,time)
                                    break
                            print()
                        else:
                            print("Insufficient Balance")
                            print()
                    except:
                        print("Enter a valid amount")
                        print()
                else:
                    print("Invalid Password")
                    print()
            else:
                print("invalid Account Number")
                print()
        except:
            print("Enter a valid Account Number")
            print()

    def cash():
        inp = input("(1) Cash Deposit\n(2) Cash Withdrawal\n(3) Money Transfer\n(4) Transaction History\n(5) Transfer History : ")
        if  inp == "1":
            Customer.d_cash()
            print()
        elif  inp == "2":
            Customer.w_cash()
            print()
        elif  inp == "3":
            Customer.cash_transfer()
            print()
        elif  inp == "4":
            Customer.history()
            print()
        elif  inp == "5":
            Customer.cash_history()
            print()
        else:
            print("Invalid Input")
            print()

    def d_cash():
        try:
            inp = int(input("Enter your Account Number :"))
            if  dbqueryone(f"SELECT STATUS FROM CUSTOMER WHERE account_num = {inp};"):
                password = input("Enter your Password")
                if password == dbqueryone(f"SELECT PASSWORD FROM CUSTOMER WHERE account_num ={inp}"):
                    try:
                        d_amount = float(input("Enter Amount :"))
                        if d_amount >0:
                            balance = dbqueryone(f"SELECT BALANCE FROM CUSTOMER WHERE account_num ={inp}") + d_amount
                            dbquery(f"UPDATE CUSTOMER SET BALANCE = {balance} WHERE account_num = {inp};")
                            print("Deposited Successful")
                            print(f"Total Balance: {balance}")
                            time = datetime.datetime.today().strftime("%Y-%m-%d %H:%M")
                            while True:
                                transaction_id = random.randint(100000,999999)
                                if transaction_id in ( dbquery(f"SELECT TRANSACTION_ID FROM BANKTRANS WHERE TRANSACTION_ID = {transaction_id}") ,dbquery(f"SELECT TRANSACTION_ID FROM CUSTTRANS WHERE TRANSACTION_ID = {transaction_id}")):
                                    continue
                                else:
                                    Customer.create_transaction(transaction_id,inp,"deposit",d_amount,time)
                                    break
                            print()
                        else:
                            print("Entered Amount Should be Positive")
                            print()
                    except:
                        print("Enter a valid amount")
                        print()
                else:
                    print("Invalid Password")
                    print()
            else:
                print("invalid Account Number")
                print()
        except:
            print("Enter a valid Account Number")
            print()

    @staticmethod
    def create_transaction(transaction_id, account_num,type,amount,datetime):
        dbquery(f"INSERT INTO  CUSTTRANS VALUES ({transaction_id}, {account_num}, '{type}', {amount}, '{datetime}')")
        mydb.commit()
    def cash_transfer_history(transaction_id, sender_account_num,reciver_account_num, amount, datetime ):
        dbquery(f"INSERT INTO  CASH_TRANSFER VALUES ({transaction_id}, {sender_account_num}, {reciver_account_num}, {amount}, '{datetime}')")
        mydb.commit()

    def delete_account():
        try:
            inp = int(input("Enter your Account Number :"))
            if  dbqueryone(f"SELECT STATUS FROM CUSTOMER WHERE account_num = {inp};"):
                password = input("Enter your Password")
                if password == dbqueryone(f"SELECT PASSWORD FROM CUSTOMER WHERE account_num ={inp}"):
                    dbquery(f"UPDATE CUSTOMER SET STATUS = False WHERE account_num = {inp};")
                    print("Account Deleted Successfully")
                    print()
                else:
                    print("Invalid Password")
                    print()
            else:
                print("Invalid Account Number")
                print()
        except:
            print("Enter a valid Account Number")
            print()


    def history():
        try:
            inp = int(input("Enter your Account Number :"))
            if  dbqueryone(f"SELECT STATUS FROM CUSTOMER WHERE account_num = {inp};"):
                password = input("Enter your Password : ")
                if password == dbqueryone(f"SELECT PASSWORD FROM CUSTOMER WHERE account_num ={inp}"):
                    print("Transaction History:")
                    print(f"Transaction ID\t\tType\t\tAmount\t\tDate Time")
                    for row in dbquery(f"SELECT * FROM CUSTTRANS WHERE ACCOUNT_NUM = {inp} ORDER BY DATE_TIME DESC"):
                        print(f"{str(row[0]).center(16," ")}{row[1].center(23," ")}{str(row[2]).center(24," ")}{str(row[3]).center(2)}")
                else:
                    print("Invalid Password")
                    print()
            else:
                print("Invalid Account Number")
                print()
        except:
            print("Enter a valid Account Number")
            print()

    def cash_history():
        try:
            inp = int(input("Enter your Account Number :"))
            if  dbqueryone(f"SELECT STATUS FROM CUSTOMER WHERE account_num = {inp};"):
                password = input("Enter your Password : ")
                if password == dbqueryone(f"SELECT PASSWORD FROM CUSTOMER WHERE account_num ={inp}"):
                    print("Transaction History:")
                    print(f"Transaction ID\t\tSender Account Number\t\tReciver Account Number\t\tAmount\t  Date Time")
                    for row in dbquery(f"SELECT * FROM CASH_TRANSFER WHERE FROM_ACCOUNT_NUM = {inp} ORDER BY DATE_TIME DESC"):
                        print(f"{str(row[0]).center(14," ")} {str(row[1]).center(21," ")} {str(row[22]).center(25," ")}{str(row[8]).center(8," ")}{row[4]}")
                else:
                    print("Invalid Password")
                    print()
            else:
                print("Invalid Account Number")
                print()
        except:
            print("Enter a valid Account Number")
            print()
    def cash_transfer():
        try:
            sender_account_num = int(input("Enter Your Account Number : "))
            if  dbqueryone(f"SELECT STATUS FROM CUSTOMER WHERE account_num = {sender_account_num};"):
                sender_password = input("Enter your Password : ")
                if sender_password == dbqueryone(f"SELECT PASSWORD FROM CUSTOMER WHERE account_num ={sender_account_num}"):
                    receiver_account_num = int(input("Enter Receiver's Account Number : "))
                    if  dbqueryone(f"SELECT STATUS FROM CUSTOMER WHERE account_num = {receiver_account_num};"):
                        amount = int(input("Enter Amount : "))
                        sender_current_balance = dbqueryone(f"SELECT BALANCE FROM CUSTOMER WHERE account_num = {sender_account_num}")
                        if amount > 0 :
                            if sender_current_balance>=amount:
                                sender_balance = sender_current_balance - amount
                                dbquery(f"UPDATE CUSTOMER SET BALANCE = {sender_balance} WHERE account_num = {sender_account_num}")
                                reciver_current_balance = dbqueryone(f"SELECT BALANCE FROM CUSTOMER WHERE account_num = {receiver_account_num}")
                                reciver_balance = reciver_current_balance + amount
                                dbquery(f"UPDATE CUSTOMER SET BALANCE = {reciver_balance} WHERE account_num = {receiver_account_num}")
                                while True:
                                    transaction_id = random.randint(100000,999999)
                                    if transaction_id in ( dbquery(f"SELECT TRANSACTION_ID FROM BANKTRANS WHERE TRANSACTION_ID = {transaction_id}") ,dbquery(f"SELECT TRANSACTION_ID FROM CUSTTRANS WHERE TRANSACTION_ID = {transaction_id}"), dbquery(f"SELECT TRANSACTION_ID FROM CASG_TRANSFER WHERE TRANSACTION_ID = {transaction_id}") ):
                                        continue
                                    else:
                                        time = datetime.datetime.today().strftime("%Y-%m-%d %H:%M")
                                        Customer.cash_transfer_history(transaction_id,sender_account_num,receiver_account_num,amount,time)
                                        print("Transaction Successful")
                                        break
                            else:
                                print("Insufficient Balance")
                        else:
                            print("Amount should be positive")
                    else:
                        print("Invalid Receiver's Account Number")
            else:
                print("Invalid Account Number")
        except:
            print("Enter a valid Account Number")
            print()
                            

                        


    
                    

#print(type(dbqueryone(f"SELECT balance FROM BANK.CUSTOMER WHERE account_num = 512068589599;")))