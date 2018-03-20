from create_sql import create_sqlite_table
from create_sql import clean_empty_values
from create_sql import meteorite_frequency_table
from create_sql import close_sqlite_db



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

    #scatter plot needs to be refactored using sql instead of pandas
    #scatter_plot(read_csv_with_pandas())

    close_sqlite_db()



if __name__ == '__main__':
    main()
