import mysql.connector as mysql
mydb=mysql.connect(host='localhost',user='root',port='3306',password='')
mycursor=mydb.cursor()
mycursor.execute('use bankmanagementsystem')
mydb.commit()

#Credit amount of User:

def credit_amount():
   name=input('Enter your account holder name:')
   date=input('Enter todays date:')
   typ=input('enter your transaction type:')
   cdt_amt=int(input('Enter your Credit amount:'))
   dbt_amt=None
   print()
   
   query='SELECT Balance FROM {}'.format(name)  # to select balance column from account holders name database.
   mycursor.execute(query)
   retrive=mycursor.fetchall() # fetch all balance entries in balance column.

   total=[]
   for x in retrive:
      total=total+[*x]      # [*x]-unpack tuple values and add all balance entries in empty total list.

   total.reverse()          # reverse()-fn can give all the entries in reverse order.
   update_balance=total[0]  # we can get latest previous balance through index position.
   t_balance=update_balance+cdt_amt # add previous balance and credit amount to get our total balance.

   # Insert Values in account holders name table.
   credit='INSERT INTO {}(Date,Type,Credit,Debit,Balance)VALUES(%s,%s,%s,%s,%s)'.format(name)
   val=(date,typ,cdt_amt,dbt_amt,t_balance)
   mycursor.execute(credit,val)
   mydb.commit()
   print(cdt_amt,': Your amount is successfully credited.')
   mydb.close()

