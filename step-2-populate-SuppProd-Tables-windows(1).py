#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 13:30:15 2018

@author: acggs
"""
import pymysql
import pandas as pd

# Populate the database with data




# Open database connection
db = pymysql.connect(host="localhost",
                     user="root",
                     passwd="mysqlpassword")
cursor=db.cursor()



cursor.execute("use supplierProduct")



#Read Supplier, Product, and SupplierProduct data from CSV
data = pd.read_csv ('data-Supplier-Product/supplier2.data', names=['id', 'name', 'status', 'city'], sep=' ', skiprows=1)
                    
data2 = pd.read_csv ('data-Supplier-Product/product2.data', names=['id', 'name', 'color', 'weight', 'city'], sep=' ', skiprows=1)
data3 = pd.read_csv ('data-Supplier-Product/supplierProduct2.data', names=['sid', 'pid', 'qty'], sep='  ', skiprows=1)




#Insert supplier data to DB
cols = ",".join([str(i) for i in data.columns.tolist()])
# Insert DataFrame recrds one bdy one.
for i,row in data.iterrows():
    sql = "INSERT INTO supplier (" +cols + ") VALUES " + str(tuple (row))    
    cursor.execute(sql)
    db.commit()


#Insert product data to DB
cols = ",".join([str(i) for i in data2.columns.tolist()])
# Insert DataFrame recrds one by one.
for i,row in data2.iterrows():
    sql = "INSERT INTO product (" +cols + ") VALUES " + str(tuple (row))    
    cursor.execute(sql)
    db.commit()

#Insert supplierproduct data to DB
cols = ",".join([str(i) for i in data3.columns.tolist()])
# Insert DataFrame recrds one by one.
for i,row in data3.iterrows():
    sql = "INSERT INTO supplierproduct2 (" +cols + ") VALUES " + str(tuple (row))    
    cursor.execute(sql)
    db.commit()




# disconnect from server
db.close()
