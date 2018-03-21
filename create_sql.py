import sqlite3
import csv


sql = sqlite3.connect('meteo.db')
cur = sql.cursor()
csv_file = open('Meteorite_Landings.csv','r', errors='ignore')
next(csv_file, None)
reader = csv.reader(csv_file)


def create_sqlite_table():

    cur.execute('''DROP TABLE IF EXISTS meteorite_data''')
    cur.execute('''CREATE TABLE IF NOT EXISTS meteorite_data
                (name TEXT UNIQUE, 
                meteo_id INTIGER PRIMARY KEY,
                nametype TEXT, 
                recclass TEXT,
                mass REAL, 
                fall TEXT, 
                year DATETIME, 
                reclat REAL,
                reclong REAL, 
                GeoLocation REAL);''')

    for row in reader:
        cur.execute('''INSERT INTO meteorite_data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''', row)

    csv_file.close()


def clean_empty_values():

    cur.execute('''DELETE FROM meteorite_data WHERE(name IS NULL OR name  = '') 
                    OR (mass IS NULL OR mass = '') OR (year IS NULL OR year = '') 
                    OR (reclat IS NULL OR reclat = '') OR (reclong IS NULL OR reclong = '') 
                    OR (GeoLocation IS NULL OR GeoLocation = '');''')


def meteorite_frequency_table():

    def create_table_meteorite_frequency():
        cur.execute('''DROP TABLE IF EXISTS meteorite_frequency''')
        cur.execute('''CREATE TABLE meteorite_frequency (year DATETIME, count INTIGER);''')

    def populate_data():
        cur.execute('''INSERT INTO meteorite_frequency SELECT year, count(*) FROM meteorite_data GROUP BY year ORDER BY COUNT(*) desc;''')

    create_table_meteorite_frequency()
    populate_data()


def close_sqlite_db():
    sql.commit()
    sql.close()
