import sqlite3
import csv


#meteo.db is the sqlite db that will be created
sql = sqlite3.connect('meteo.db')
cur = sql.cursor()
csv_file = open('Meteorite_Landings.csv','r', errors='ignore')
next(csv_file, None)
reader = csv.reader(csv_file)


def create_sqlite_table():

    #Setup Initial meteorite_data table, if the table exists delete it (this stops an error when running the script and the tables already exist)
    cur.execute('''DROP TABLE IF EXISTS meteorite_data''')
    #creates meteorite_data table with the same column names as the csv file
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
    #iterates through the table
    for row in reader:
        cur.execute('''INSERT INTO meteorite_data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''', row)

    #close the csv connection
    csv_file.close()


def clean_empty_values():
    #Deleting Null Values
    cur.execute('''DELETE FROM meteorite_data WHERE(name IS NULL OR name  = '') 
                    OR (mass IS NULL OR mass = '') OR (year IS NULL OR year = '') 
                    OR (reclat IS NULL OR reclat = '') OR (reclong IS NULL OR reclong = '') 
                    OR (GeoLocation IS NULL OR GeoLocation = '');''')


def meteorite_frequency_table():

    #Create a new table with only year and count per year
    def create_table_meteorite_frequency():
        #Check if meteorite_frequency exists, if it does it deletes the table
        cur.execute('''DROP TABLE IF EXISTS meteorite_frequency''')
        #Create a new table called meteorite_frequency that will contain a year column and a count column
        cur.execute('''CREATE TABLE meteorite_frequency (year DATETIME, count INTIGER);''')

    #inset sql query results into meteorite_frequency table 
    def populate_data():
        cur.execute('''INSERT INTO meteorite_frequency SELECT year, count(*) FROM meteorite_data GROUP BY year ORDER BY COUNT(*) desc;''')

    create_table_meteorite_frequency()
    populate_data()


#Reuse this several times 
def close_sqlite_db():
    sql.commit()
    sql.close()
