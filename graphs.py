import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sqlite3

def visualizations_year_frequency():

    """Put data into a pandas dataframe for additional cleaning and graphing"""
    #use pandas to retrieve sqlite tables
    conn = sqlite3.connect('meteo.db')
    meteorites_frequency = pd.read_sql_query('SELECT year, count FROM meteorite_frequency ORDER BY year DESC;', conn)
    conn.close()

    #Concert year to datetime then remove NA values
    meteorites_frequency['year'] = pd.to_datetime(meteorites_frequency['year'], errors='coerce')
    meteorites_frequency = meteorites_frequency.dropna()

    #This grabs just the year from the year column since the data seems to be all in the format 1/1/year
    meteorites_frequency['year_only'] = meteorites_frequency.year.map(lambda x: x.strftime('%Y'))

    #Use pandas to convert strings into numbers(int)
    meteorites_frequency['year_only'] = meteorites_frequency['year_only'].astype(int)
    meteorites_frequency['count'] = meteorites_frequency['count'].astype(int)

    #This is to get rid of a lingering incorrect year from the future
    meteorites_frequency = meteorites_frequency[meteorites_frequency.year_only <= 2018]

    last_50_years = meteorites_frequency[0:50]


    def matplotlib_frequency_line():

        """Matplotlib line graph showing frequency per year"""
        x = meteorites_frequency['year_only']
        y = meteorites_frequency['count']

        plt.plot(x, y)

        plt.xlabel('Time (Years)')
        plt.ylabel('Frequency')
        plt.title('Number of Meteorite Landings per Year')
        plt.grid(True)
        plt.savefig("graphs/frequency_line.png")
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
        plt.savefig("graphs/frequency_line_last_50.png")
        plt.show()


    def matplotlib_frequency_bar():

        """Matplotlib bar graph showing frequency per year"""
        x = meteorites_frequency['year_only']
        y = meteorites_frequency['count']

        plt.bar(x, y)

        plt.xlabel('Time (Years)')
        plt.ylabel('Frequency')
        plt.title('Number of Meteorites per Year')
        plt.grid(True)
        plt.savefig("graphs/frequency_bar_last_50.png")
        plt.show()


    def matplotlib_frequency_bar_last_50():

        """Matplotlib bar graph showing frequency per year"""
        x = last_50_years['year_only']
        y = last_50_years['count']

        plt.bar(x, y)

        plt.xlabel('Time (Years)')
        plt.ylabel('Frequency')
        plt.title('Number of Meteorites per Year')
        plt.grid(True)
        plt.savefig("graphs/frequency_bar.png")
        plt.show()


    matplotlib_frequency_line()
    matplotlib_frequency_bar()
    matplotlib_frequency_line_last_50()
    matplotlib_frequency_bar_last_50()


def visualizations_year_max_mass():

    """Put data into a pandas dataframe for additional cleaning and graphing"""
    #use pandas to retrieve sqlite tables
    conn = sqlite3.connect('meteo.db')
    meteorites_max_mass = pd.read_sql_query('SELECT year, mass FROM meteorite_data GROUP BY year ORDER BY year DESC;', conn)
    conn.close()

    #Concert year to datetime then remove NA values
    meteorites_max_mass['year'] = pd.to_datetime(meteorites_max_mass['year'], errors='coerce')
    meteorites_max_mass = meteorites_max_mass.dropna()

    #This grabs just the year from the year column since the data seems to be all in the format 1/1/year
    meteorites_max_mass['year_only'] = meteorites_max_mass.year.map(lambda x: x.strftime('%Y'))

    #Use pandas to convert strings into numbers(int)
    meteorites_max_mass['year_only'] = meteorites_max_mass['year_only'].astype(int)
    meteorites_max_mass['mass'] = meteorites_max_mass['mass'].astype(float)

    #convert mass in grams to kg
    meteorites_max_mass['mass'] = meteorites_max_mass['mass'] / 1000

    #This is to get rid of a lingering incorrect year from the future
    meteorites_max_mass = meteorites_max_mass[meteorites_max_mass.year_only <= 2018]

    last_50_years_max_mass = meteorites_max_mass[0:50]

    def matplotlib_year_max_mass_line():

        """Matplotlib line graph showing frequency per year"""
        x = meteorites_max_mass['year_only']
        y = meteorites_max_mass['mass']

        plt.plot(x, y)

        plt.xlabel('Time (Years)')
        plt.ylabel('Maximum Mass (kg)')
        plt.title('Maximum Mass of Meteorite Landings per Year in kg')
        plt.grid(True)
        plt.savefig("graphs/year_max_mass_line.png")
        plt.show()

    def matplotlib_year_max_mass_bar():

        """Matplotlib bar graph showing frequency per year"""
        x = meteorites_max_mass['year_only']
        y = meteorites_max_mass['mass']

        plt.bar(x, y)

        plt.xlabel('Time (Years)')
        plt.ylabel('Maximum Mass (kg)')
        plt.title('Maximum Mass of Meteorite Landings per Year in kg')
        plt.grid(True)
        plt.savefig("graphs/year_max_mass_bar_last_50.png")
        plt.show()

    def matplotlib_year_max_mass_line_last_50():

        """Matplotlib line graph showing frequency per year"""
        x = last_50_years_max_mass['year_only']
        y = last_50_years_max_mass['mass']

        plt.plot(x, y)
        plt.xlabel('Time (Years)')
        plt.ylabel('Maximum Mass (kg)')
        plt.title('Maximum Mass of Meteorite Landings per Year in kg')
        plt.grid(True)
        plt.savefig("graphs/year_max_mass_line_last_50.png")
        plt.show()

    def matplotlib_year_max_mass_bar_last_50():

        """Matplotlib bar graph showing frequency per year"""
        x = last_50_years_max_mass['year_only']
        y = last_50_years_max_mass['mass']

        plt.bar(x, y)

        plt.xlabel('Time (Years)')
        plt.ylabel('Maximum Mass (kg)')
        plt.title('Maximum Mass of Meteorite Landings per Year in kg')
        plt.grid(True)
        plt.savefig("graphs/year_max_mass_bar.png")
        plt.show()

    matplotlib_year_max_mass_line()
    matplotlib_year_max_mass_bar()
    matplotlib_year_max_mass_line_last_50()
    matplotlib_year_max_mass_bar_last_50()








































def visualizations_year_sum_mass():

    """Put data into a pandas dataframe for additional cleaning and graphing"""
    #use pandas to retrieve sqlite tables
    conn = sqlite3.connect('meteo.db')
    meteorites_sum_mass = pd.read_sql_query('SELECT year, SUM(mass) FROM meteorite_data GROUP BY year ORDER BY year DESC;', conn)
    conn.close()

    #Concert year to datetime then remove NA values
    meteorites_sum_mass['year'] = pd.to_datetime(meteorites_sum_mass['year'], errors='coerce')
    meteorites_sum_mass = meteorites_sum_mass.dropna()

    #This grabs just the year from the year column since the data seems to be all in the format 1/1/year
    meteorites_sum_mass['year_only'] = meteorites_sum_mass.year.map(lambda x: x.strftime('%Y'))

    #Use pandas to convert strings into numbers(int)
    meteorites_sum_mass['year_only'] = meteorites_sum_mass['year_only'].astype(int)
    meteorites_sum_mass['mass'] = meteorites_sum_mass['mass'].astype(float)

    #convert mass in grams to kg
    meteorites_sum_mass['mass'] = meteorites_sum_mass['mass'] / 1000

    #This is to get rid of a lingering incorrect year from the future
    meteorites_sum_mass = meteorites_sum_mass[meteorites_sum_mass.year_only <= 2018]

    last_50_years_sum_mass = meteorites_sum_mass[0:50]