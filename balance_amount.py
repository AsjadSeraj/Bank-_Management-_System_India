import mysql.connector as mysql
mydb=mysql.connect(host='localhost',user='root',port='3306',password='')
mycursor=mydb.cursor()
mycursor.execute('use bankmanagementsystem')
mydb.commit()

# To check users account balance:

def balance():
    name=input('Enter your name:')
    print()
    
    bal='SELECT Balance FROM {}'.format(name)
    mycursor.execute(bal)
    retrive=mycursor.fetchall()

    total=[]
    for x in retrive:
        total=total+[*x]

    total.reverse()
    update_balance=total[0]

    print('Your total balance is:',update_balance)