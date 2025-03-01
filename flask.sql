from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL connection settings
username = 'your_username'
password = 'your_password'
host = 'your_host'
database = 'your_database'

# Create a connection to the database
cnx = mysql.connector.connect(
    user=username,
    password=password,
    host=host,
    database=database
)

# Create a cursor object to execute SQL queries
cursor = cnx.cursor()

# Route to render the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submissions
@app.route('/submit', methods=['POST'])
def submit():
    # Get the form
