from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def get_db_connection():
   conn = psycopg2.connect(
        host='db',
        database='mydb',
        user='user',
        password='password'
    )
   return conn



@app.route('/')
def home():
    return 'Hello World!'

@app.route('/data')
def get_data():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM items')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)