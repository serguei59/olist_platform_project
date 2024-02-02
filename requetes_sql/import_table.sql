-- Execute this command to create the tables
-- sqlite3 olist.db < requetes_sql/import_table.sql 2>/dev/null


.import --csv --skip 1 data/state_name.csv StateName 
.import --csv --skip 1 data/geolocation_dataset.csv Geolocation 
.import --csv --skip 1 data/customers_dataset.csv Customers 
.import --csv --skip 1 data/sellers_dataset.csv Sellers 
.import --csv --skip 1 data/orders_dataset.csv Orders 
.import --csv --skip 1 data/product_category_name_translation.csv ProductCategoryName 
.import --csv --skip 1 -v data/products_dataset.csv Products 
.import --csv --skip 1 -v data/order_items_dataset.csv OrderItem 
.import --csv --skip 1 -v data/order_payments_dataset.csv Payments  
.import --csv --skip 1 -v data/order_review_dataset_clean.csv Reviews 
.import --csv --skip 1 -v data/olist_order_reviews_dataset.csv Reviews 


