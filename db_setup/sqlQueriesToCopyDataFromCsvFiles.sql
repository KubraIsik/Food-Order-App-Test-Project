-- remove id columns(first column) in the csv files, before run this sql queries.
-- change 'path_to_your_csv/restaurants.csv' with full path where related .csv file is located for each query.
-- locate .csv files in Program Files\PostgreSQL\14\data\pg_data folder if data could not be copied from other locations.
-- run queries one by one to ensure correctly copy

-- copy data from csv file restaurants.csv into restaurants table
COPY restaurants(name, address, phone)
FROM 'path_to_your_csv/restaurants.csv'
DELIMITER ','
CSV HEADER;

-- copy data from excel file categories.csv into categories table
COPY categories(name)
FROM 'path_to_your_csv/categories.csv'
DELIMITER ','
CSV HEADER;

-- copy data from excel file restaurant_category.csv into restaurant_category table
COPY restaurant_category(category_id, restaurant_id)
FROM 'path_to_your_csv/restaurant_category.csv' 
DELIMITER ',' 
CSV HEADER;

-- copy data from excel file menu_items.csv into menu_items table
COPY menu_items(name, description,price,category_id,restaurant_id)
FROM 'path_to_your_csv/menu_items.csv' 
DELIMITER ',' 
CSV HEADER;