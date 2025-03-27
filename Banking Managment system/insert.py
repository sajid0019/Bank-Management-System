import os
import csv
from database import *
import re
import random


def insert_emp():
    with open("Pyhthonemp.csv","r+") as data_obj:
     reader_obj = csv.reader(data_obj)
     header = next(reader_obj)
     for a,b,c,d,e,f in reader_obj:
        empid = random.randint(10000000, 99999999)
        if dbquery(f"SELECT EMPLOYEE_ID FROM EMP WHERE EMPLOYEE_ID = {empid}"):
            continue
        else:
            job = random.choice(("CLERK","ASSOCIATE","ANALYST","SALESMAN"))
            dbquery(f"INSERT INTO EMP VALUES ({empid},'{a}', {b} ,'{c}', {d},'{e}','{job}','{f}',True)")
            mydb.commit()
          

def insert_customer():
    with open("Pyhthonemp.csv","r+") as data_obj:
     reader_obj = csv.reader(data_obj)
     header = next(reader_obj)
     for a,b,c,d,e in reader_obj:
         while True:
            account_num = random.randint(100000000000,999999999999)
            acno = dbquery(f"SELECT ACCOUNT_NUM FROM CUSTOMER WHERE ACCOUNT_NUM = {account_num}") 
            if acno:
                continue
            else:
                 balance = random.randint(9000,456779)
                 dbquery(f"INSERT INTO CUSTOMER VALUES ('{a}',{b}, {balance}, '{c}' ,'{d}',{e},{account_num},True)")
                 break