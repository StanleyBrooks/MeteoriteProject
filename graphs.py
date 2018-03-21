import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sqlite3

def visualizations():

    """Put data into a pandas dataframe for additional cleaning and graphing"""
    #use pandas to retrieve sqlite tables
    conn = sqlite3.connect('meteo.db')
    meteorites = pd.read_sql_query('SELECT year, count FROM meteorite_frequency ORDER BY year DESC;', conn)
    conn.close()

    #Concert year to datetime then remove NA values
    meteorites['year'] = pd.to_datetime(meteorites['year'], errors='coerce')
    meteorites = meteorites.dropna()

    #This grabs just the year from the year column since the data seems to be all in the format 1/1/year
    meteorites['year_only'] = meteorites.year.map(lambda x: x.strftime('%Y'))

    #Use pandas to convert strings into numbers(int)
    meteorites['year_only'] = meteorites['year_only'].astype(int)
    meteorites['count'] = meteorites['count'].astype(int)

    #This is to get rid of a lingering incorrect year from the future
    meteorites = meteorites[meteorites.year_only <= 2018]

    last_50_years = meteorites[0:50]


    def matplotlib_frequency_line():

        """Matplotlib line graph showing frequency per year"""
        x = meteorites['year_only']
        y = meteorites['count']

        plt.plot(x, y)

        plt.xlabel('Time (Years)')
        plt.ylabel('Frequency')
        plt.title('Number of Meteorite Landings per Year')
        plt.grid(True)
        plt.savefig("matplotlib_frequency_line.png")
        plt.show()


    def matplotlib_frequency_line_last_50():

        """Matplotlib line graph showing frequency per year"""
        x = last_50_years['year_only']
        y = last_50_years['count']

        plt.plot(x, y)

        plt.xlabel('Time (Years)')
        plt.ylabel('Frequency')
        plt.title('Number of Meteorite Landings per Year')
        plt.grid(True)
        plt.savefig("matplotlib_frequency_line_last_50.png")
        plt.show()


    def matplotlib_frequency_bar():

        """Matplotlib bar graph showing frequency per year"""
        x = meteorites['year_only']
        y = meteorites['count']

        plt.bar(x, y)

        plt.xlabel('Time (Years)')
        plt.ylabel('Frequency')
        plt.title('Number of Meteorites per Year')
        plt.grid(True)
        plt.savefig("matplotlib_frequency_bar.png")
        plt.show()


    def matplotlib_frequency_bar_line_last_50():

        """Matplotlib bar graph showing frequency per year"""
        x = last_50_years['year_only']
        y = last_50_years['count']

        plt.bar(x, y)

        plt.xlabel('Time (Years)')
        plt.ylabel('Frequency')
        plt.title('Number of Meteorites per Year')
        plt.grid(True)
        plt.savefig("matplotlib_frequency_bar.png")
        plt.show()


    matplotlib_frequency_line()
    matplotlib_frequency_bar()
    matplotlib_frequency_line_last_50()
    matplotlib_frequency_bar_line_last_50()