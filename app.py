import sqlite3
import uuid
import datetime
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
#app.config['EXPLAIN_TEMPLATE_LOADING'] = True

def get_hardware_id():
    return str(uuid.getnode())

def init_db():
    conn = sqlite3.connect('demo.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hardware_id TEXT NOT NULL,
            utc_time TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/current')
def get_current():
    return jsonify({
        'hardware_id': get_hardware_id(),
        'utc_time': datetime.datetime.utcnow().isoformat() + 'Z'
    })

@app.route('/api/save', methods=['POST'])
def save_record():
    hardware_id = get_hardware_id()
    utc_time = datetime.datetime.utcnow().isoformat() + 'Z'

    conn = sqlite3.connect('demo.db')
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO records (hardware_id, utc_time) VALUES (?, ?)',
        (hardware_id, utc_time)
    )
    conn.commit()
    conn.close()

    return jsonify({'status': 'saved', 'hardware_id': hardware_id, 'utc_time': utc_time})

@app.route('/api/records')
def get_records():
    conn = sqlite3.connect('demo.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM records ORDER BY timestamp DESC LIMIT 10')
    records = cursor.fetchall()
    conn.close()

    return jsonify([{
        'id': r[0],
        'hardware_id': r[1],
        'utc_time': r[2],
        'timestamp': r[3]
    } for r in records])

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
