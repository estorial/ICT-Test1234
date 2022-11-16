#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 13:36:59 2018

@author: acggs
"""


# works with windows
import pymysql



#Access a database

# Open database connection
db = pymysql.connect(host="localhost",           #address of the server
                     user="root",                #user name
                     passwd="mysqlpassword")      #password

cursor=db.cursor()



cursor.execute("use supplierProduct")


# select columns
# this a query, but it's only text
sql1="""SELECT id, name FROM product"""
cursor.execute(sql1)

#select rows 
sql2="""select * from product
      where name='Screw'"""
      
#groupby: how many products per city?
sql3="""select count(id), city from product
      group by city"""
  
#select all suppliers whose name starts with an S
#%S   starts with S
#%S   ends with S
#%S%  have s in any position
sql4="""select * from supplier
      where name like '%S'"""

#groupby: how many people per city?
sql5="""select count(id), city from supplier
      group by city"""
    
sql6="""select supplier.name, product.name from
        supplier, product, supplierProduct2
        where supplier.id = supplierProduct2.sid and
              product.id = supplierProduct2.pid """

sql7 = """SELECT name
FROM supplier
LEFT JOIN supplierproduct2
ON  supplier.id = supplierproduct2.sid
WHERE supplierproduct2.qty = 200 AND supplierproduct2.pid = 'P1'"""

cursor.execute(sql1)
cursor.execute(sql2)
cursor.execute(sql3)
cursor.execute(sql4)
cursor.execute(sql5)
cursor.execute(sql6)
cursor.execute(sql7)
result=cursor.fetchall()
print (result)


db.close()





