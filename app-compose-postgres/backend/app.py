from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

conn = psycopg2.connect(
    dbname=os.environ['DB_NAME'],
    user=os.environ['DB_USER'],
    password=os.environ['DB_PASS'],
    host=os.environ['DB_HOST']
)
cur = conn.cursor()

@app.route('/users', methods=['GET'])
def get_users():
    cur.execute("SELECT * FROM users;")
    rows = cur.fetchall()
    return jsonify(rows)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    cur.execute("INSERT INTO users (name) VALUES (%s) RETURNING id;", (data['name'],))
    conn.commit()
    return jsonify({"id": cur.fetchone()[0]}), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
