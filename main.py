from flask import Flask, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Configuration for MySQL connection
MYSQL_HOST = 'mysqlseverzbs001.mysql.database.azure.com'
MYSQL_USER = 'u_instance_owner'
MYSQL_PASSWORD = 'Welcome01!'
MYSQL_DATABASE = 'db01'

def check_mysql_connection():
    try:
        connection = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE
        )
        if connection.is_connected():
            connection.close()
            return True
    except Error as e:
        print(f"Error: {e}")
        return False

@app.route('/check_connection', methods=['GET'])
def check_connection():
    if check_mysql_connection():
        return jsonify(status="OK"), 200
    else:
        return jsonify(status="False"), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
