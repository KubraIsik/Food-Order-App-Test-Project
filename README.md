# Food Order App Testing Project

This project contains automated tests for a food order application. Tests are applied on "yemeksepeti.com" website."
The tests are written using `pytest` and `selenium`, and involve retrieving data from a database and simulating user interactions on the website.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Database Setup](#database-setup)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

This project aims to automate the testing of a food order application. The tests ensure that the website functionality works as expected, including menu displays, shopping cart operations, and user interactions.

## Installation

Follow these steps to set up the project on your local machine:

1. Clone the repository:
    ```bash
    git clone https://github.com/username/food-order-app-tests.git
    cd food-order-app-tests
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

food-order-app-tests
│
├── README.md
├── .gitignore
├── db_utils.py
├── helpers.py
├── requirements.txt
│
├── data
│ ├── data.xlsx
│ ├── get_data.py
│ ├── globalConstants.py
│── pages
│ │ ├── orderCheckout_page.py
│ │ └── restaurant_page.py
│── tests
│ ├── test_cartOperations.py
  └── test_restaurantMenu.py
