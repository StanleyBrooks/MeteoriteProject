from create_sql import create_sqlite_table
from create_sql import clean_empty_values
from create_sql import meteorite_frequency_table
from create_sql import close_sqlite_db

from graphs import visualizations_year_frequency
from graphs import visualizations_year_max_mass


def main():

    print('=' * 30)
    print('Creating SQLite Database...')
    print('=' * 30)
    print('Creating table meteorite_data...')

    create_sqlite_table()

    print('Completed successfully')
    print('=' * 30)

    print('Deleting null values in SQLite Database...')
    
    clean_empty_values()
    
    print('Completed successfully')
    print('=' * 30)

    print('Creating meteorite_frequency table...')
    print('Populating table and performing count operation...')
    
    meteorite_frequency_table()
    
    print('Completed successfully')
    print('=' * 30)

    print('Completed successfully')
    print('=' * 30)

    close_sqlite_db()

    visualizations_year_frequency()

    visualizations_year_max_mass()


if __name__ == '__main__':
    main()
