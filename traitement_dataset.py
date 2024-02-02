import sqlite3
from pathlib import Path
import subprocess
import os

def make_data_cleaning():
    
    #connection = sqlite3.connect("olist_db.db")


    with sqlite3.connect("olist_db.db") as connection:
        cursor = connection.cursor()


#requetes creation bdd olist_db
        sql_file = open("requetes_sql/create_table.sql")
        sql_as_string = sql_file.read()
        cursor.executescript(sql_as_string)
        print('creation olist_db ok')
        connection.commit()
#requetes imports des tables
        #sql_file2 = open("requetes_sql/import_table.sql") : cette requete ne fonctionne pas ici
        
        #j applique le code d import a chaque table 
        db_name = Path('olist_db.db').resolve()
      
        csv_file = Path('data/customers_dataset.csv').resolve()
        result = subprocess.run(['sqlite3',
                         str(db_name),
                         '-cmd',
                         '.mode csv',
                         '.import --skip 1 ' + str(csv_file).replace('\\','\\\\')
                                 +' Customers'],
                        capture_output=True)
                              
        print('import table Customers olist_db ok')
        connection.commit() 

        csv_file = Path('data/geolocation_dataset.csv').resolve()
        result = subprocess.run(['sqlite3',
                         str(db_name),
                         '-cmd',
                         '.mode csv',
                         '.import --skip 1 ' + str(csv_file).replace('\\','\\\\')
                                 +' Geolocation'],
                        capture_output=True)
        
        print('import table Geolocation olist_db ok')
        connection.commit()


        csv_file = Path('data/olist_order_reviews_dataset.csv').resolve()
        result = subprocess.run(['sqlite3',
                         str(db_name),
                         '-cmd',
                         '.mode csv',
                         '.import --skip 1 ' + str(csv_file).replace('\\','\\\\')
                                 +' Reviews'],
                        capture_output=True)
        
        print('import table Reviews 1/2 olist_db ok')
        connection.commit()

        csv_file = Path('data/order_items_dataset.csv').resolve()
        result = subprocess.run(['sqlite3',
                         str(db_name),
                         '-cmd',
                         '.mode csv',
                         '.import --skip 1 ' + str(csv_file).replace('\\','\\\\')
                                 +' OrderItem'],
                        capture_output=True)
        
        print('import table Orderitem  olist_db ok')
        connection.commit()

        csv_file = Path('data/order_payments_dataset.csv').resolve()
        result = subprocess.run(['sqlite3',
                         str(db_name),
                         '-cmd',
                         '.mode csv',
                         '.import --skip 1 ' + str(csv_file).replace('\\','\\\\')
                                 +' Payments'],
                        capture_output=True)
        
        print('import table Payments olist_db ok')
        connection.commit()

        csv_file = Path('data/order_review_dataset.csv').resolve()
        result = subprocess.run(['sqlite3',
                         str(db_name),
                         '-cmd',
                         '.mode csv',
                         '.import --skip 1 ' + str(csv_file).replace('\\','\\\\')
                                 +' Reviews'],
                        capture_output=True)
        
        print('import table reviews 2/2 olist_db ok')
        connection.commit()

        csv_file = Path('data/orders_dataset.csv').resolve()
        result = subprocess.run(['sqlite3',
                         str(db_name),
                         '-cmd',
                         '.mode csv',
                         '.import --skip 1 ' + str(csv_file).replace('\\','\\\\')
                                 +' Orders'],
                        capture_output=True)
        
        print('import table Orders olist_db ok')
        connection.commit()

        csv_file = Path('data/product_category_name_translation.csv').resolve()
        result = subprocess.run(['sqlite3',
                         str(db_name),
                         '-cmd',
                         '.mode csv',
                         '.import --skip 1 ' + str(csv_file).replace('\\','\\\\')
                                 +' ProductCategoryName'],
                        capture_output=True)
        
        print('import ProductCategoryName olist_db ok')
        connection.commit()

        csv_file = Path('data/products_dataset.csv').resolve()
        result = subprocess.run(['sqlite3',
                         str(db_name),
                         '-cmd',
                         '.mode csv',
                         '.import --skip 1 ' + str(csv_file).replace('\\','\\\\')
                                 +' Products'],
                        capture_output=True)
        
        print('import table Products olist_db ok')
        connection.commit()

        csv_file = Path('data/sellers_dataset.csv').resolve()
        result = subprocess.run(['sqlite3',
                         str(db_name),
                         '-cmd',
                         '.mode csv',
                         '.import --skip 1 ' + str(csv_file).replace('\\','\\\\')
                                 +' Sellers'],
                        capture_output=True)
        
        print('import table Sellers olist_db ok')
        connection.commit()

        csv_file = Path('data/state_name.csv').resolve()
        result = subprocess.run(['sqlite3',
                         str(db_name),
                         '-cmd',
                         '.mode csv',
                         '.import --skip 1 ' + str(csv_file).replace('\\','\\\\')
                                 +' StateName'],
                        capture_output=True)
        
        
        print('import table Sellers olist_db ok')
        connection.commit()

        
        
# execution nettoyage.py
        cmd_nettoyage = '1_nettoyage.py'
        os.system(cmd_nettoyage)

        connection.commit()
# execution featuring.py
        cmd_feature_engineering = '2_feature_engineering.py'
        os.system(cmd_feature_engineering)
        
        connection.commit()
 
        
        



        