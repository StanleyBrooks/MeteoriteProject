from create_sql import create_sqlite_table
from create_sql import clean_empty_values
from create_sql import meteorite_frequency_table
from create_sql import close_sqlite_db

from graphs import visualizations_year_frequency
from graphs import visualizations_year_max_mass

from world_map import world_maps

#terminal output formatting
line_break = ('=' * 50)
line_break_fancy = ('*' * 50)

#This script runs the program and displays basic output to the user in the prompt
def main():
    """this script runs the following functions in the following order: 
    create_sqlite_table()
    clean_empty_values()
    meteorite_frequency_table()
    close_sqlite_db()
    visualizations_year_frequency()
    visualizations_year_max_mass()
    world_maps()
    """

    print(line_break)
    print('Creating SQLite Database...')
    print(line_break)
    print('Creating table meteorite_data...')

    create_sqlite_table()

    print('table meteorite_datao created successfully')
    print(line_break)

    print('Deleting null values in SQLite Database...')
    
    clean_empty_values()
    
    print('null values deleted successfully')
    print(line_break)

    print('Creating meteorite_frequency table...')
    print('Populating table and performing count operation...')
    
    meteorite_frequency_table()
    
    print('Completed successfully')
    print(line_break)

    print('Database created successfully')
    print(line_break)

    print('Closing Database')
    print(line_break)

    close_sqlite_db()

    print('Database closed successfully')
    print(line_break)

    print('Creating matplotlib graphs')
    print(line_break)

    print('Creating year/frequency graph')
    print(line_break)

    visualizations_year_frequency()

    print('Creating year/mass graph')
    print(line_break)

    visualizations_year_max_mass()

    print('Matplotlib graphs created successfully')
    print(line_break)

    print('Creating World Map with Bokeh')
    print(line_break)

    #Bokeh maps (one mapped from json, the other with googles API)
    world_maps()

    print('World Map created successfully')
    print(line_break)

    print('All graphs located in ./graphs')
    print(line_break)

    print(line_break_fancy)
    print('Program Finished')
    print(line_break_fancy)
    print(line_break)

#this makes the script main() as long as it is not being imported into another script.
if __name__ == '__main__':
    main()
