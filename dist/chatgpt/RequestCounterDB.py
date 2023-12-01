import sqlite3
from datetime import date


class RequestCounterDB:
    def __init__(self, db_name="request_counts.db"):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        self.setup_db()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    def setup_db(self):
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS requests (
                     ip_address TEXT PRIMARY KEY,
                     request_count INTEGER,
                     last_request_date TEXT)''')
        self.conn.commit()

    def get_request_count(self, ip_address):
        c = self.conn.cursor()
        c.execute("SELECT request_count, last_request_date FROM requests WHERE ip_address=?", (ip_address,))
        result = c.fetchone()

        if result:
            request_count, last_request_date = result
            if last_request_date != str(date.today()):
                request_count = 0
                c.execute("UPDATE requests SET request_count=?, last_request_date=? WHERE ip_address=?",
                          (request_count, str(date.today()), ip_address))
                self.conn.commit()
        else:
            request_count = 0
            last_request_date = str(date.today())
            c.execute("INSERT INTO requests (ip_address, request_count, last_request_date) VALUES (?, ?, ?)",
                      (ip_address, request_count, last_request_date))
            self.conn.commit()

        return request_count

    def increment_request_count(self, ip_address):
        c = self.conn.cursor()
        c.execute("UPDATE requests SET request_count=request_count+1 WHERE ip_address=?", (ip_address,))
        self.conn.commit()
