import mysql.connector as mysql
mydb=mysql.connect(host='localhost',user='root',port='3306',password='')
mycursor=mydb.cursor()
mycursor.execute('use bankmanagementsystem')
mydb.commit()

#delete Account holders account:
def delete_account():
    name=input('Enter your account holder name:')
    delet="DELETE FROM account_holders WHERE Name='{}'".format(name)
    mycursor.execute(delet)
    delt='DROP TABLE IF EXISTS {}'.format(name)
    mycursor.execute(delt)
    print('Account holder account deleted.')
    mydb.commit()
    mydb.close()
    print()
