from sqlalchemy import create_engine
from sqlalchemy import text  

#connfigure engine and connection
engine = create_engine('sqlite:///db/cartOrder.db')

#create connection
conn = engine.connect()

#create table with SQL Query

query = text("""
            CREATE TABLE IF NOT EXISTS "transaction"(
            transactionID VARCHAR(255),
            item_name VARCHAR(255) NOT NULL,
            item_qty INT NOT NULL,
            item_price REAL NOT NULL,
            total_price REAL NOT NULL,
            disc INT NOT NULL,
            disc_price REAL NOT NULL
            );
            """)

conn.execute(query)

conn.close()    

def insert_to_db(final_cart):
    try:
        # Create SQLite database and connection
        engine = create_engine('sqlite:///db/cartOrder.db')
        conn = engine.connect()

        # Insert each row from the DataFrame into the database
        for i, row in final_cart.iterrows():
            transaction_id = row['transaction_id']
            item_name = row['index']
            quantity = row['quantity']
            price = row['price']
            total_price = row['total_price']
            discount = row['disc']
            discounted_price = row['disc_price']

            query = text("""
                         INSERT INTO "transaction" (transactionID, item_name, item_qty, item_price, total_price, disc, disc_price)    
                         VALUES (:transactionID, :item_name, :quantity, :price, :total_price, :discount, :discounted_price)""")

            conn.execute(query, 
                         {'transactionID':transaction_id,
                          'item_name': item_name,
                          'quantity': quantity,
                          'price':price,
                          'total_price':total_price,
                          'discount':discount,
                          'discounted_price':discounted_price})

        print("Transaction has been inserted into database")

    except Exception as e:
        print(f"ERROR: {e}")

    finally:
        # Close the connection
        conn.close()

