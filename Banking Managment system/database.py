# import mysql.connector

# mydb = mysql.connector.connect(
#     host="127.0.0.1",
#     port = 3306,
#     user="root",
#     password="asdfghji",
#     database="bank"
# )
import sqlite3
mydb = sqlite3.connect('bank.db')
cursor = mydb.cursor()
def createcustomertable():
    cursor.execute('''CREATE TABLE IF NOT EXISTS CUSTOMER(
                   USERNAME VARCHAR(30) NOT NULL,
                   AGE INTEGER NOT NULL,
                   BALANCE FLOAT NOT NULL,
                   PLACE VARCHAR(50) NOT NULL,
                   PASSWORD VARCHAR(20) NOT NULL,
                   PHONE BIGINT NULL,
                   ACCOUNT_NUM BIGINT PRIMARY KEY,
                   STATUS BOOLEAN NOT NULL) ''' )
    
def customer_transaction_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS CUSTTRANS(
                    TRANSACTION_ID BIGINT PRIMARY KEY,
                    ACCOUNT_NUM BIGINT NOT NULL,
                    TYPE VARCHAR(20) NOT NULL,
                    AMOUNT FLOAT NOT NULL,
                    DATE_TIME DATETIME NOT NULL, 
                    CONSTRAINT fk_cust_trans_account_num FOREIGN KEY (ACCOUNT_NUM) REFERENCES CUSTOMER(ACCOUNT_NUM)) ''' )

def create_employee_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS EMP(
                    EMPLOYEE_ID BIGINT PRIMARY KEY,
                    ENAME VARCHAR(20) NOT NULL,
                    AGE INTEGER NOT NULL,
                    ADDRESS VARCHAR(50) NOT NULL,
                    PHONE BIGINT NOT NULL,
                    EMAIL VARCHAR(50) NOT NULL,
                    JOB VARCHAR(50) NOT NULL,
                    PASSWORD VARCHAR(20) NOT NULL,
                    STATUS BOOLEAN NOT NULL) ''' )
def bank_modification_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS BANKTRANS(
                    TRANSACTION_ID BIGINT PRIMARY KEY,
                    EMPLOYEE_ID BIGINT NOT NULL,
                    ENAME VARCHAR(20) NOT NULL,
                    TYPE VARCHAR(20) NOT NULL,
                    DATE_TIME DATETIME NOT NULL, 
                    CONSTRAINT fk_mod_num FOREIGN KEY (EMPLOYEE_ID) REFERENCES EMP(EMPLOYEE_ID)) ''' )
                        
def cash_transfer_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS CASH_TRANSFER(
                    TRANSACTION_ID BIGINT PRIMARY KEY,
                    FROM_ACCOUNT_NUM BIGINT NOT NULL,
                    TO_ACCOUNT_NUM BIGINT NOT NULL,
                    AMOUNT FLOAT NOT NULL,
                    DATE_TIME DATETIME NOT NULL, 
                    CONSTRAINT fk_from_account_num FOREIGN KEY (FROM_ACCOUNT_NUM) REFERENCES CUSTOMER(ACCOUNT_NUM),
                    CONSTRAINT fk_to_account_num FOREIGN KEY (TO_ACCOUNT_NUM) REFERENCES CUSTOMER(ACCOUNT_NUM)) ''' )
def dbquery(str):  
    cursor.execute(str)
    result = cursor.fetchall()
    mydb.commit()
    return result


def dbqueryone(str):  
    cursor.execute(str)
    result = cursor.fetchone()
    mydb.commit()
    return result[0]



mydb.commit()

createcustomertable()
customer_transaction_table()
create_employee_table() 
bank_modification_table()
cash_transfer_table()
    
 
    
