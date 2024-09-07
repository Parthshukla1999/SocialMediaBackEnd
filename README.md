# SocialMediaBackEnd Project setup

Installation

Prerequisites

1. Install Python

Install python ( I Used python version 3.12) and python-pip. Follow the steps from the below reference document based on your Operating System. Reference: https://docs.python-guide.org/starting/installation/

2. Install PostgreSQL

Install PostgreSQL-16. Follow the steps form the below reference document based on your Operating System. Reference: [https://www.postgresql.org]

3. Setup virtual environment

Open one folder Terminal where you want to clone the project and run command to create a virtual environment

python3 -m venv env_name


# Activate virtual environment
source envs/bin/activate

4. Clone git repository

git clone HTTP URL

5. Install requirements

cd folder Name/

pip install -r requ.txt

6. Open .env file 

add database details which is given below:-
DB_NAME = YOUR DATABASE NAME,
DB_USER = DATABASE USER,
DB_PASSWORD = DATABASE PASSWORD,
DB_HOST = DATABASE HOST(LOCALHOST),
DB_PORT = DATABASE PORT(STANDARD PORT NUMBER :5432)


# Make migrations
1.python manage.py makemigrations

2.python manage.py migrate

# Run the server
python manage.py runserver

# your server is up on port 8000
Try opening http://localhost:8000 in the browser. Now you are good to go
