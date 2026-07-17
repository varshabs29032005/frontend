import mysql.connector
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

def get_products():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="29032005",
        database="productdb"
    )

    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT id, name, price FROM products")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows

@app.route('/api/products')
def api_products():

    sort = request.args.get('sort', 'id')

    allowed = {'id', 'name', 'price'}

    col = sort if sort in allowed else 'id'

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="29032005",
        database="productdb"
    )

    cur = conn.cursor(dictionary=True)

    cur.execute(f"SELECT id, name, price FROM products ORDER BY {col}")

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(rows)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)