# Food Order App Testing Project

This project contains automated tests for a food order application. Tests are applied on [Yemek Sepeti](https://www.yemeksepeti.com/) website."
Tests are only applied on restaurant pages and shopping cart. A basic database created to create test data and automation test interactions.
The tests are written using `pytest` and `selenium`, and involve retrieving data from a database to be used as expected outputs of the test cases.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Database Setup](#database-setup)
- [Running Tests](#running-tests)
- [Contact](#contact)

## Introduction

This project aims to automate the testing of a food order application. The tests ensure that the website functionality works as expected, including menu displays, shopping cart operations, and user interactions.

## Installation

Follow these steps to set up the project on your local machine:

1. Clone the repository:
    ```bash
    git clone [https://github.com/username/food-order-app-tests.git](https://github.com/KubraIsik/Food-Order-App-Test-Project.git)
    cd Food-OrderAapp-Test-Project
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Project Structure

Here's an overview of the project structure:

```
food-order-app-tests
│
├── README.md
├── .gitignore
├── db_utils.py
├── helpers.py
├── requirements.txt
├── data
│ ├── data.xlsx
│ ├── get_data.py
│ └── globalConstants.py
│── db_setup
│ ├── ERDdiagramofDB.pgerd.png
│ ├── sqlFileToCreateDBTables.sql
│ └── sqlQueriesToCopyDataFromCsvFiles.sql
│── pages
│ ├── orderCheckout_page.py
│ └── restaurant_page.py
│── tests
│ ├── test_cartOperations.py
│ └── test_restaurantMenu.py
└── .env
```

## Database Setup
To quick overview of the database, here is the Entity Relationship Diagram of the db:
![ERD_image](https://github.com/KubraIsik/Food-Order-App-Test-Project/blob/main/db_setup/ERDdiagramofDB.pgerd.png)

To retrieve data and work with this database:

1. Ensure your PostgreSQL server is running.
2. Create a new database called "food_order_db":
    ```bash
    createdb food_order_db
    ```
3. Run the SQL script to create the necessary tables:
    ```bash
    psql -d food_order_db -f db_setup/sqlFileToCreateDBTables.sql
    ```
4. (Optional) Read descriptions on the sql file and Run the data SQL script to insert initial data:
    ```bash
    psql -d food_order_db -f db_setup/sqlQueriesToCopyDataFromCsvFiles.sql
    ```

*To be able connect db while running pytest project:*
    Make sure to update the database connection settings in your `.env` file 
    Included .env file to your project should include this lines with your information.
    ```
    DB_USER = 'your_db_user_name'
    DB_PASSWORD = 'your_password'
    ``` 
    or 
    the configuration file of your project accordingly
        Change code lines inside `db_utils.py` file with your information(db user name and password).

## Running Tests

To run the tests, use the following commands:

1. Ensure the database is set up and the web application is running.
2. Execute the tests using pytest:
    ```bash
    pytest
    ```
    
## Contact
I would like to here from you: do not hesitate to reach out for any questions, comments or contributions to the project!

Kübra Nazlıhan IŞIK - [kuisik@gmail.com](kuisik@gmail.com)

Project Link: [https://github.com/username/food-order-app-tests](https://github.com/KubraIsik/Food-Order-App-Test-Project.git)
    

