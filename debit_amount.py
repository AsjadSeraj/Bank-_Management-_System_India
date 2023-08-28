import mysql.connector as mysql
mydb=mysql.connect(host='localhost',user='root',port='3306',password='')
mycursor=mydb.cursor()
mycursor.execute('use bankmanagementsystem')
mydb.commit()

# Debit amount of User:
def debit_amount():
    name=input('Enter your name:')
    date=input('Enter todays date:')
    typ=input('Enter your transaction type:')
    dbt_amt=int(input('Enter your Amount:'))
    cdt_amt=None
    print()
    
    query='SELECT Balance FROM {} '.format(name)   # to select balance column from account holders name database.
    mycursor.execute(query)
    retrive=mycursor.fetchall()                    # fetch all balance entries in balance column.

    total=[]
    for x in retrive:
        total=total+[*x]              # [*x]-unpack tuple values and add all balance entries in empty total list.

    total.reverse()                   # reverse()-fn can give all the entries in reverse order.
    update_balance=total[0]           # we can get latest previous balance through index position.
    t_amount=update_balance-dbt_amt   # subtract previous balance and credit amount to get our total balance.

    # Insert Values in account holders name table.
    debit='INSERT INTO {} (Date,Type,Credit,Debit,Balance)VALUES(%s,%s,%s,%s,%s)'.format(name)
    amount=(date,typ,cdt_amt,dbt_amt,t_amount)
    mycursor.execute(debit,amount)
    print(dbt_amt,':Your amount is successfully debited')
    mydb.commit()
    mydb.close()
