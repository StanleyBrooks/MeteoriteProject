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


    def matplotlib_frequency_bar_last_50():

        """Matplotlib bar graph showing frequency per year (Last 50 Years)"""
        x = np.array(last_50_years['year_only'])
        y = np.array(last_50_years['count'])

        #Set the graph axis (Dont want it to go under 0 for y(median - std messes with the ymin))
        plt.ylim([0,last_50_years['count'].max()])
        plt.xlim([(last_50_years['year_only'].min()), (last_50_years['year_only'].max())])

        y_mean = [np.mean(y)]*len(x)
        y_median = [np.median(y)]*len(x)
        y_std = [np.std(y)]*len(x)
        
        plt.plot(x, y_mean, label='Mean', linestyle='--', color="#4E6620")
        plt.plot(x, y_median, label='Median', linestyle='--', color="orange")
        plt.plot(x, y_std, label='Standard Deviation', linestyle='--', color="#FF0000")
        plt.fill_between(x, (y_median - np.std(y)), (y_median + np.std(y)), label="One Standard Deviation from Median (-/+)", color="#D8F69E")
        plt.legend(loc='upper right', prop={'size': 6})

        plt.bar(x, y)
        plt.xlabel('Time (Years)')
        plt.ylabel('Frequency of Meteorite Landings')
        plt.title('Frequency of Meteorite Landings In The Last 50 Years')
        plt.grid(True)
        plt.savefig("graphs/frequency_bar_last_50.png")

        plt.show()

    def matplotlib_frequency_line_last_50():

        """Matplotlib line graph showing frequency per year (Last 50 Years)"""
        x = np.array(last_50_years['year_only'])
        y = np.array(last_50_years['count'])

        #Set the graph axis
        plt.ylim([0,last_50_years['count'].max()])
        plt.xlim([(last_50_years['year_only'].min()), (last_50_years['year_only'].max())])

        y_mean = [np.mean(y)]*len(x)
        y_median = [np.median(y)]*len(x)
        y_std = [np.std(y)]*len(x)

        plt.plot(x, y_mean, label='Mean', linestyle='--', color="#4E6620")
        plt.plot(x, y_median, label='Median', linestyle='--', color="orange")
        plt.plot(x, y_std, label='Standard Deviation', linestyle='--', color="#FF0000")
        plt.fill_between(x, y_median - np.std(y), y_median + np.std(y), label="One Standard Deviation from Median (-/+)", color="#D8F69E")
        plt.legend(loc='upper right', prop={'size': 6})

        plt.plot(x, y)

        plt.xlabel('Time (Years)')
        plt.ylabel('Frequency of Meteorite Landings')
        plt.title('Frequency of Meteorite Landings In The Last 50 Years')
        plt.grid(True)
        plt.savefig("graphs/frequency_line_last_50.png")
        plt.show()

    def matplotlib_frequency_bar():

        """Matplotlib bar graph showing frequency per year"""
        x = np.array(meteorites_frequency['year_only'])
        y = np.array(meteorites_frequency['count'])

        #Set the graph axis
        plt.ylim([0,meteorites_frequency['count'].max()])
        plt.xlim([(meteorites_frequency['year_only'].min()), (meteorites_frequency['year_only'].max())])

        y_mean = [np.mean(y)]*len(x)
        y_median = [np.median(y)]*len(x)
        y_std = [np.std(y)]*len(x)

        plt.plot(x, y_mean, label='Mean', linestyle='--', color="#4E6620")
        plt.plot(x, y_median, label='Median', linestyle='--', color="orange")
        plt.plot(x, y_std, label='Standard Deviation', linestyle='--', color="#FF0000")
        plt.fill_between(x, y_median - np.std(y), y_median + np.std(y), label="One Standard Deviation from Median (-/+)", color="#D8F69E")
        plt.legend(loc='upper right', prop={'size': 6})

        plt.bar(x, y)

        plt.xlabel('Time (Years)')
        plt.ylabel('Frequency of Meteorite Landings')
        plt.title('Frequency of Meteorite Landings In The Entire Data Set')
        plt.grid(True)
        plt.savefig("graphs/frequency_bar.png")
        plt.show()

    def matplotlib_frequency_line():

        """Matplotlib line graph showing frequency per year"""
        x = np.array(meteorites_frequency['year_only'])
        y = np.array(meteorites_frequency['count'])

        #Set the graph axis
        plt.ylim([0,meteorites_frequency['count'].max()])
        plt.xlim([(meteorites_frequency['year_only'].min()), (meteorites_frequency['year_only'].max())])

        y_mean = [np.mean(y)]*len(x)
        y_median = [np.median(y)]*len(x)
        y_std = [np.std(y)]*len(x)

        plt.plot(x, y_mean, label='Mean', linestyle='--', color="#4E6620")
        plt.plot(x, y_median, label='Median', linestyle='--', color="orange")
        plt.plot(x, y_std, label='Standard Deviation', linestyle='--', color="#FF0000")
        plt.fill_between(x, y_median - np.std(y), y_median + np.std(y), label="One Standard Deviation from Median (-/+)", color="#D8F69E")
        plt.legend(loc='upper right', prop={'size': 6})

        plt.plot(x, y)

        plt.xlabel('Time (Years)')
        plt.ylabel('Frequency of Meteorite Landings')
        plt.title('Frequency of Meteorite Landings In The Entire Data Set')
        plt.grid(True)
        plt.savefig("graphs/frequency_line.png")
        plt.show()

    def matplotlib_frequency_line_last_50_lob():

        """Matplotlib line graph showing frequency per year (Last 50 Years)"""
        x = np.array(last_50_years['year_only'])
        y = np.array(last_50_years['count'])

        #Set the graph axis
        plt.ylim([0,last_50_years['count'].max()])
        plt.xlim([(last_50_years['year_only'].min()), (last_50_years['year_only'].max())])

        plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), label="Line of Best Fit", linestyle='--', color="red")
        
        plt.legend(loc='upper right', prop={'size': 10})

        plt.plot(x, y)

        plt.xlabel('Time (Years)')
        plt.ylabel('Frequency of Meteorite Landings')
        plt.title('Line of Best Fit applied to Frequency of Meteorite Landings over Time')
        plt.grid(True)
        plt.savefig("graphs/frequency_line_last_50_lob.png")
        plt.show()


    matplotlib_frequency_bar_last_50()
    matplotlib_frequency_line_last_50()
    matplotlib_frequency_bar()
    matplotlib_frequency_line()
    matplotlib_frequency_line_last_50_lob()


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
        x = np.array(meteorites_max_mass['year_only'])
        y = np.array(meteorites_max_mass['mass'])

        #Set the graph axis
        plt.ylim([0,meteorites_max_mass['mass'].max()])
        plt.xlim([(meteorites_max_mass['year_only'].min()), (meteorites_max_mass['year_only'].max())])

        y_mean = [np.mean(y)]*len(x)
        y_median = [np.median(y)]*len(x)
        y_std = [np.std(y)]*len(x)

        #Shows the Mean with a dotted line
        plt.plot(x, y_mean, label='Mean', linestyle='--', color="#4E6620")
        #shows Median
        plt.plot(x, y_median, label='Median', linestyle='--', color="orange")
        plt.plot(x, y_std, label='Standard Deviation', linestyle='--', color="#FF0000")
        #This line shades 1 standard deviation from the median
        plt.fill_between(x, y_median - np.std(y), y_median + np.std(y), label="One Standard Deviation from Median (-/+)", color="#D8F69E")
        plt.legend(loc='upper right', prop={'size': 6})

        plt.plot(x, y)

        plt.xlabel('Time (Years)')
        plt.ylabel('Maximum Mass (kg)')
        plt.title('Maximum Mass of Meteorite Landings per Year in kg')
        plt.grid(True)
        plt.savefig("graphs/year_max_mass_line.png")
        plt.show()

    def matplotlib_year_max_mass_bar():

        """Matplotlib bar graph showing frequency per year"""
        x = np.array(meteorites_max_mass['year_only'])
        y = np.array(meteorites_max_mass['mass'])

        #Set the graph axis
        plt.ylim([0,meteorites_max_mass['mass'].max()])
        plt.xlim([(meteorites_max_mass['year_only'].min()), (meteorites_max_mass['year_only'].max())])

        y_mean = [np.mean(y)]*len(x)
        y_median = [np.median(y)]*len(x)
        y_std = [np.std(y)]*len(x)

        plt.plot(x, y_mean, label='Mean', linestyle='--', color="#4E6620")
        plt.plot(x, y_median, label='Median', linestyle='--', color="orange")
        plt.plot(x, y_std, label='Standard Deviation', linestyle='--', color="#FF0000")
        plt.fill_between(x, y_median - np.std(y), y_median + np.std(y), label="One Standard Deviation from Median (-/+)", color="#D8F69E")
        plt.legend(loc='upper right', prop={'size': 6})

        plt.bar(x, y)

        plt.xlabel('Time (Years)')
        plt.ylabel('Maximum Mass (kg)')
        plt.title('Maximum Mass of Meteorite Landings per Year in kg')
        plt.savefig("graphs/year_max_mass_bar_last_50.png")
        plt.show()

    def matplotlib_year_max_mass_line_last_50():

        """Matplotlib line graph showing frequency per year"""
        x = np.array(last_50_years_max_mass['year_only'])
        y = np.array(last_50_years_max_mass['mass'])

        #Set the graph axis
        plt.ylim([0,last_50_years_max_mass['mass'].max()])
        plt.xlim([(last_50_years_max_mass['year_only'].min()), (last_50_years_max_mass['year_only'].max())])

        y_mean = [np.mean(y)]*len(x)
        y_median = [np.median(y)]*len(x)
        y_std = [np.std(y)]*len(x)

        plt.plot(x, y_mean, label='Mean', linestyle='--', color="#4E6620")
        plt.plot(x, y_median, label='Median', linestyle='--', color="orange")
        plt.plot(x, y_std, label='Standard Deviation', linestyle='--', color="#FF0000")
        plt.fill_between(x, y_median - np.std(y), y_median + np.std(y), label="One Standard Deviation from Median (-/+)", color="#D8F69E")
        plt.legend(loc='upper right', prop={'size': 6})

        plt.plot(x, y)
        plt.xlabel('Time (Years)')
        plt.ylabel('Maximum Mass (kg)')
        plt.title('Maximum Mass of Meteorite Landings per Year in kg')
        plt.grid(True)
        plt.savefig("graphs/year_max_mass_line_last_50.png")
        plt.show()

    def matplotlib_year_max_mass_bar_last_50():

        """Matplotlib bar graph showing frequency per year"""
        x = np.array(last_50_years_max_mass['year_only'])
        y = np.array(last_50_years_max_mass['mass'])

        #Set the graph axis
        plt.ylim([0,last_50_years_max_mass['mass'].max()])
        plt.xlim([(last_50_years_max_mass['year_only'].min()), (last_50_years_max_mass['year_only'].max())])

        y_mean = [np.mean(y)]*len(x)
        y_median = [np.median(y)]*len(x)
        y_std = [np.std(y)]*len(x)

        plt.plot(x, y_mean, label='Mean', linestyle='--', color="#4E6620")
        plt.plot(x, y_median, label='Median', linestyle='--', color="orange")
        plt.plot(x, y_std, label='Standard Deviation', linestyle='--', color="#FF0000")
        plt.fill_between(x, y_median - np.std(y), y_median + np.std(y), label="One Standard Deviation from Median (-/+)", color="#D8F69E")
        plt.legend(loc='upper right', prop={'size': 6})

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
