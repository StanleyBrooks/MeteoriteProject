import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import numpy as np

def visualizations():

    conn = sqlite3.connect('meteo.db')
    meteorites = pd.read_sql_query('select year, count from meteorite_frequency ORDER BY year ASC;', conn)
    conn.close()

    meteorites['year'] = pd.to_datetime(meteorites['year'], errors='coerce')
    meteorites = meteorites.dropna()
    meteorites['year_only'] = meteorites.year.map(lambda x: x.strftime('%Y'))

    meteorites['year_only'] = meteorites['year_only'].apply(pd.to_numeric)
    meteorites['count'] = meteorites['count'].apply(pd.to_numeric)


    def matplotlib_frequency_line():

        x = meteorites['year_only']
        y = meteorites['count']

        plt.plot(x, y)

        plt.xlabel('Time (Years)')
        plt.ylabel('Frequency')
        plt.title('Number of Meteorites per Year')
        plt.grid(True)
        plt.savefig("matplotlib_frequency_line.png")
        plt.show()


    def matplotlib_frequency_bar():

        x = meteorites['year_only']
        y = meteorites['count']

        plt.bar(x, y)

        plt.xlabel('Time (Years)')
        plt.ylabel('Frequency')
        plt.title('Number of Meteorites per Year')
        plt.grid(True)
        plt.savefig("matplotlib_frequency_bar.png")
        plt.show()


    matplotlib_frequency_line()
    matplotlib_frequency_bar()