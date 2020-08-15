#!/usr/bin/python3

# Turn on debug mode.
import cgitb

cgitb.enable()

# Print necessary headers.
print("Content-Type: text/html")
print()

# Connect to the database.
import pymysql
conn = pymysql.connect(
    db='ecommercedb',
    user='root',
    port=3308, 
    passwd='Vigneshbala@95!',
    host='localhost')
cursor = conn.cursor()

# Insert some example data.
import random
print("Cursor ready...");     

try:
    cursor.execute("""insert into Product values 
    ('%d','%s','%d')""" %(random.randint(1,1000000),"Mouse",248));
        #cursor.execute(query);
    conn.commit()
except pymysql.Error as e:
    print("Exception occurred",e )
    conn.rollback()    

# Print the contents of the database.
cursor.execute("SELECT * FROM Product")
print([(r[0], r[1]) for r in cursor.fetchall()])
