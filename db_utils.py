import psycopg2
from data.globalConstants import DB_PASSWORD, DB_USER 

# Function to establish database connection
def get_db_connection():
    conn = psycopg2.connect(
        dbname = "food_order_db", # info will be hide by .env variables
        user = DB_USER, #"postgres",
        password = DB_PASSWORD, #"12345",
        host = "localhost"
    )
    return conn

# Function to close database connection
def close_db_connection(conn):
    conn.close()

# Function to fetch restaurant IDs from the database
def fetch_restaurant_ids(cursor):
    query = "SELECT restaurant_id FROM restaurants"
    cursor.execute(query)
    restaurant_ids = [row[0] for row in cursor.fetchall()]
    return restaurant_ids

# Function to fetch categories for a specific restaurant from the database
def fetch_categories_for_restaurant(cursor, restaurant_id):
    query = """SELECT c.name FROM categories c  
                    join restaurant_category rc on rc.category_id = c.category_id 
                    join restaurants r on rc.restaurant_id = r.restaurant_id  
                WHERE r.restaurant_id = %s"""
    cursor.execute(query, (restaurant_id,))
    categories = [row[0] for row in cursor.fetchall()]
    return categories

# Function to fetch count categories for a specific restaurant from the database
def fetch_count_categories_for_restaurant(cursor, restaurant_id):
    query = """SELECT Count(*) FROM categories c  
                    join restaurant_category rc on rc.category_id = c.category_id 
                    join restaurants r on rc.restaurant_id = r.restaurant_id  
                WHERE r.restaurant_id = %s"""
    cursor.execute(query, (restaurant_id,))
    num_categories = [row[0] for row in cursor.fetchall()] # list has only 1 row number of counted rows
    return num_categories[0] # return only 1 integer, first index of the list

# Function to fetch menu_items for a specific restaurant from the database, category_id
def fetch_menu_items_for_restaurant(cursor, restaurant_id):
    query = """SELECT m.name, m.price FROM menu_items m  
                    join categories c on m.category_id = c.category_id 
                    join restaurants r on m.restaurant_id = r.restaurant_id  
                WHERE r.restaurant_id = %s
                ORDER BY m.id"""
                #and m.category_id = 4 
                #ORDER BY m.id"""  # category_id filter to check only that category elements
    cursor.execute(query, (restaurant_id,))
    menu_item_name_price = [row for row in cursor.fetchall()]

    # format retrieved price values:
    # Format prices in the retrieved data, e.g. "273 TL"
    formatted_menu_items = [(name, f"{str(price)} TL") for name, price in menu_item_name_price]

    return formatted_menu_items #menu_item_name_price

# Function to fetch count menu_items for a specific restaurant from the database, category_id
def fetch_count_menu_items_for_restaurant(cursor, restaurant_id):
    query = """SELECT Count(*) FROM menu_items m  
                    join categories c on m.category_id = c.category_id 
                    join restaurants r on m.restaurant_id = r.restaurant_id  
                WHERE r.restaurant_id = %s
                """
                #and m.category_id = 4 
                #""" # category_id filter to check only that category elements
    cursor.execute(query, (restaurant_id,))
    menu_item_name_price = [row[0] for row in cursor.fetchall()] # list has only 1 row number of counted rows
    
    return menu_item_name_price[0] # return only 1 integer, first index of the list 