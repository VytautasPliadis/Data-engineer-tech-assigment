import os
import csv
import sqlite3
from sqlite3 import Error


# create sqlite folder
os.chdir('..')
path=os.getcwd()
if not os.path.exists(path+'\\raw_data\\sqlite'):
    os.mkdir(path+'\\raw_data\\sqlite')


def csvSqlite(csv_file,conn,cursor):
    # Insert data into table
    with open(csv_file, 'r') as fin:
        dr = csv.DictReader(fin)
        info = [(i['VendorID'], i['tpep_pickup_datetime'], i['tpep_dropoff_datetime'], i['passenger_count'], i['trip_distance'], i['RatecodeID'], i['store_and_fwd_flag'], i['PULocationID'], i['DOLocationID'], i['payment_type'], i['fare_amount'], i['extra'], i['mta_tax'], i['tip_amount'], i['tolls_amount'], i['improvement_surcharge'], i['total_amount'], i['congestion_surcharge'], i['airport_fee']) for i in dr]
    cursor.executemany(
    "insert into yellow_tripdata (VendorID,tpep_pickup_datetime,tpep_dropoff_datetime,passenger_count,trip_distance,RatecodeID,store_and_fwd_flag,PULocationID,DOLocationID,payment_type,fare_amount,extra,mta_tax,tip_amount,tolls_amount,improvement_surcharge,total_amount,congestion_surcharge,airport_fee) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", info)
    conn.commit()

if __name__ == '__main__':
    # make path dir for sqlite
    path=os.getcwd()
    print(path)

    if not os.path.exists(path+'\\raw_data\\sqlite'):
        os.mkdir(path+'\\raw_data\\sqlite')
    
    conn = None
    conn = sqlite3.connect(path+'\\raw_data\\sqlite\\yellow_tripdata.db')
    print(sqlite3.version)
    cursor = conn.cursor()

    # create table for first time
    try:
        cursor.execute('create table yellow_tripdata (VendorID,tpep_pickup_datetime,tpep_dropoff_datetime,passenger_count,trip_distance,RatecodeID,store_and_fwd_flag,PULocationID,DOLocationID,payment_type,fare_amount,extra,mta_tax,tip_amount,tolls_amount,improvement_surcharge,total_amount,congestion_surcharge,airport_fee);')
        conn.commit()
        print('Table created')
    except:
        pass 

    # Insert data into table/change current directory
    data_path = os.getcwd()
    os.chdir(data_path+'\\raw_data\\splitted_csv')
    #loop through files in a folder
    for count, f in enumerate(os.listdir()):
        csvSqlite(f,conn,cursor)
        print(f)

    conn.close()