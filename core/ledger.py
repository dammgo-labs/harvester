import sqlite3

class Ledger:
    def __init__(self, db_path="ledger.db"):
        self.conn = sqlite3.connect(db_path)
        self._init_db()

    def _init_db(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS processed_urls (
                url TEXT PRIMARY KEY,
                processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()

    def is_processed(self, url: str) -> bool:
        cursor = self.conn.cursor()
        cursor.execute('SELECT 1 FROM processed_urls WHERE url = ?', (url,))
        return cursor.fetchone() is not None

    def mark_processed(self, url: str):
        cursor = self.conn.cursor()
        cursor.execute('INSERT OR IGNORE INTO processed_urls (url) VALUES (?)', (url,))
        self.conn.commit()
