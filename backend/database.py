import sqlite3

conn = sqlite3.connect('mediAI.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS diagnoses (
    id INTEGER PRIMARY KEY,
    doctor_id TEXT NOT NULL,
    patient_id TEXT NOT NULL,
    diagnosis TEXT NOT NULL,
    confidence REAL NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')
conn.commit()
