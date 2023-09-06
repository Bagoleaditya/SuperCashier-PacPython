from sqlalchemy import create_engine
from sqlalchemy import text  

#connfigure engine and connection
engine = create_engine('sqlite:///db/cart_order.db')

#create connection
conn = engine.connect()

#create table with SQL Query

query = text("""
            CREATE TABLE IF NOT EXISTS "transaction"(
            id VARCHAR(255) PRIMARY KEY,
            item_name VARCHAR(255),
            item_qty INT,
            item_price REAL,
            disc INT,
            disc_price REAL
            );
            """)

conn.execute(query)

conn.close()    


