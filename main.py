from create_account import *
from delete import *
from credit_amount import *
from debit_amount import *
from balance_amount import *
import mysql.connector as mysql     #connect mysql server
mydb=mysql.connect(host='localhost',user='root',port='3306',password='')
mycursor=mydb.cursor()
mycursor.execute('use bankmanagementsystem')    # to execute created database 
mydb.commit()

'''create database table of our project
db='CREATE DATABASE bankmanagementsystem'
mycursor.execute(db)
mydb.commit()
print('Database table created successfully.')'''

print('Create your account:1 \nCredit your amount:2\nDebit your amount:3\nCheck your Balance:4\nDelete your account:5')
inpt=int(input("Enter your number:"))  # take input to user 

if(inpt==1):
    create_account()
elif(inpt==5):
    delete_account()
elif(inpt==2):
    credit_amount()
elif(inpt==3):
    debit_amount()
elif(inpt==4):
    balance()
else:
    print('Your number is invalid!!')

