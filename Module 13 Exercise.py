
'''
from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/prime/<int:num>', methods=['GET'])
def calculate_prime(num):
    if num < 2:
        return jsonify({"Number": num, "isPrime": False})
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    return jsonify({"Number": num, "isPrime": is_prime})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True, use_reloader=False)
'''


from flask import Flask, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def create_db_connection():
    try:
        connection = mysql.connector.connect(
            user="Suman",
            password="Pokhara@2024",
            host="localhost",
            port="3306",
            database="flight_game",
            charset="utf8mb4",
            collation="utf8mb4_general_ci"
        )
        return connection
    except Error as err:
        print(f"Error: '{err}'")
        return None

database = create_db_connection()

def fetch_airports(icao_code):
    if not database:
        print("Database connection failed.")
        return None

    cursor = database.cursor()
    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    try:
        cursor.execute(sql, (icao_code,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return {
                "ICAO": icao_code,
                "Name": result[0],
                "Location": result[1]
            }
        return None
    except Error as err:
        print(f"Error fetching data: {err}")
        return None

@app.route('/airport/<string:icao_code>', methods=['GET'])
def get_airport_info(icao_code):
    airport = fetch_airports(icao_code.upper())
    if airport:
        return jsonify(airport)
    else:
        return jsonify({"error": "Invalid Input: Please enter a valid ICAO code"}), 400

if __name__ == '__main__':
    if database:
        app.run(host='127.0.0.1', port=5000, debug=True, use_reloader=False)
    else:
        print("Failed to connect to the database.")


