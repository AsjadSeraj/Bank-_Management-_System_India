import mysql.connector as mysql
mydb=mysql.connect(host='localhost',user='root',port='3306',password='')
mycursor=mydb.cursor()
mycursor.execute('use bankmanagementsystem')
mydb.commit()

def create_account():
    '''create account holder table:
    acc_hold='CREATE TABLE account_holders(AccountNo VARCHAR(255),Name VARCHAR(255),Contact VARCHAR(255),Email VARCHAR(255),Date_of_Birth VARCHAR(255))'
    mycursor.execute(acc_hold)
    mydb.commit()
    print('Account holder table is created successfully.')'''

    # Insert account holders details in table:

    acc_no=int(input('Enter your account number:'))
    acc_name=input('Enter your Name:')
    cont=int(input('Enter your Contact Number:'))
    email=input('Enter your Email address:')
    dob=input('Enter your Date of birth:')
    details='INSERT INTO account_holders(AccountNo,Name,Contact,Email,Date_of_Birth)VALUES(%s,%s,%s,%s,%s)'
    acc_hold=(acc_no,acc_name,cont,email,dob)
    mycursor.execute(details,acc_hold)
    mydb.commit()
    print('Account Holders details inserted are successfully.')
    print()

    #create Account holder name table:

    name_table='CREATE TABLE {} (Date VARCHAR(255),Type VARCHAR(255),Credit INT,Debit INT,Balance INT)'.format(acc_name)
    mycursor.execute(name_table)
    print('Account Holder name table created successfully.')
    t_balance=0
    cdt_amt=0
    dbt_amt=0
    v_in='INSERT INTO {}(Credit,Debit,Balance)VALUES(%s,%s,%s)'.format(acc_name)
    v=(cdt_amt,dbt_amt,t_balance)
    mycursor.execute(v_in,v)
    mydb.commit()
    mydb.close()
    

