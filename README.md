<div style="text-align: right">
By: Stanley Brooks 3/30/2018
</div>

# <center>Meteorite Landings Data Analysis
### <center>CodeLouisville Project - Python for Data


### This project requires:

>> * `bokeh` - to graph data
>> * `csv`- to read source file
>> * `json` - for the world graph (json data creates country borders)
>> * `matplotlib` - to graph data
>> * `numpy` - to help process and graph data
>> * `pandas` - to help clean and graph data (I found the pandas dataframe to be very helpful while cleaning and interacting with the dataset)
>> * `requests` - used to gather json data from website (for bokeh patches of country boarders)
>> * `sqlite3` - to create and interact with a sqlite database

### How to run the project: 

1)  Put the following files in the same directory:
>> * `create_sql.py`
>> * `graphs.py`
>> * `Meteorite_Landings.csv` -This is a copy of the dataset that can also be downloaded at https://data.nasa.gov/Space-Science/Meteorite-Landings/ak9y-cwf9.
>> * `ProjectRUN.py`
>> * `world_map.py`
>> * `README.MD`

2) There must also be a folder named `'graphs'` in the main directory, it can be empty

3) RUN the script `ProjectRUN.py`

4) The terminal will give you further information on script, create an sqlite database and output graphs to ./graphs

<br></br>
# <center>Outline of Project & Project Requirements

#### 1)  Problem that I am analyzing: 

    
* Are the frequency of all meteorite landings equally distributed?

* Are the meteorites masses the same size on average now as they have been in the past?
  - Are meteorites heavier now then they have been in the past?
  >- mass = (kg)
  >- now = (last 50 years)
  >- past = (entire dataset)

* Are the geographical locations of Meteorite Landings equally distributed worldwide?

---
## <center> Brief Overview:

I hope to accomplish these questions by using a comprehensive list of known meteorite landings from the Meteoritical Society
that can be obtained at https://data.nasa.gov/Space-Science/Meteorite-Landings/ak9y-cwf9.
From this data I have primarily used the information about the date, mass and locations (lat and long) of meteorites to figure:
    
* the amount of meteorites that fall each year
* The mass(kg) of meteorites for each year
* Geographic Locations (lat, long) of each meteorite

<br></br>

---
#### 2)  Include SQL database where your data will be stored and manipulated.  You need to include a script that sets up/creates your database
AND
#### 3)  You must include a Python script used to fetch data from a data source and load it into your SQL database
---
* This snippet of code creates a meteo.db sqlite database opens the csv file in read mode and passes it to a csv reader
```python
        sql = sqlite3.connect('meteo.db')
        cur = sql.cursor()
        csv_file = open('Meteorite_Landings.csv','r', errors='ignore')
        next(csv_file, None)
        reader = csv.reader(csv_file)

```

* This snippet of code creates the main table (meteorite_data) from the csv file.  There are also several other smaller tables created from the information in this table like (count and total_mass_kg)

```python
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

```

<br></br>
#### 4)  You must include a Python script to retrieve the data from your SQL database into a Python object
---

* This is primarily located in the graphs.py file that is included.  Data is taken from the SQL database and loaded into a pandas python object (dataframe) to be further processed(cleaned) and passed to matplotlib and bokeh for graphing

```python
        conn = sqlite3.connect('meteo.db')
        meteorites = pd.read_sql_query('SELECT year, count FROM meteorite_frequency ORDER BY year DESC;', conn)
        conn.close()

        last_50_years = meteorites[0:50]
```

<br></br>
#### 5)  You must include a Python script to modify your data so as to prepare it for visualization

---
* This happens in 2 places in the project.  The first time is in the create_sql.py file (specifically in the function clean_empty_values) and is done through sqlite querries to remove rows with null values so the csv data can be succesfully passed to the sqlite database (meteo.db)
```python
        cur.execute('''DELETE FROM meteorite_data WHERE(name IS NULL OR name  = '') 
                        OR (mass IS NULL OR mass = '') OR (year IS NULL OR year = '') 
                        OR (reclat IS NULL OR reclat = '') OR (reclong IS NULL OR reclong = '') 
                        OR (GeoLocation IS NULL OR GeoLocation = '');''')
```



* The second time this happens is after the data is pulled out of the sqlite database and inserted into a python object (pandas dataframe) in `graphs.py`.  This is done to further clean the data in preperation for graphing.  Most of the issues I ran into were with the date column, which contained dates that all started with 1/1/(year).  The month and day paramaters were just place holders, so I employed several stratagies to remove the superfluous data.
            
* Convert year to datetime then remove NA values
```python
        meteorites['year'] = pd.to_datetime(meteorites['year'], errors='coerce')
        meteorites = meteorites.dropna()
```

* This grabs just the year from the year column since the data seems to be all in the format 1/1/year
```python
        meteorites['year_only'] = meteorites.year.map(lambda x: x.strftime('%Y'))
```

* Use pandas to convert strings into numbers(int)
```python
        meteorites['year_only'] = meteorites['year_only'].astype(int)
        meteorites['count'] = meteorites['count'].astype(int)
```

* This is to get rid of a lingering incorrect year from the future\
```python
        meteorites = meteorites[meteorites.year_only <= 2018]

```
<br></br>
#### 6)  Visualize the results of your analysis using Matplotlib, Seaborn, Bokeh or another Python Data Visualization library. Your results cannot be a plaintext representation and you are encouraged to explore a visualization approach that clearly supports a conclusion/result of the analysis of your data.
---
* Multiple graphs are made using matplotlib and bokeh, they are sent to the /graphs directory when the script is ran.


TESTING:This script has been tested on multiple computers and should work just fine on and windows machine.  I have not tested it in a mac or unix environment, however it should work just fine (hopefully)

<br></br>
---















<div><center>

![Bar graph of the number of meteorites that hit the earth each year](/graphs/frequency_bar_last_50.png "Frequency of Meteorites per Year")
![](/graphs/frequency_bar_last_50.png)
![](/graphs/frequency_line.png)
![](/graphs/frequency_line_last_50.png)
![](/graphs/year_max_mass_bar.png)
![](/graphs/year_max_mass_line.png)
![](/graphs/year_max_mass_line_last_50.png)

</div>

# <center> CONCLUSION:(outline)

* Are meteorite landings happening at a faster rate now then they have been in the past?
 - The data is mixed, it appears that there have been more meteorites recorded in the past 50 years but that can be explained by many different factors.
 
 
* Are meteorites heavier now (mass) then they have been in the past?
- Other than a couple of outliers and plenty of reasons why we record more data now than in the past, it does not appear that meteorites are heavier now than they used to be.


* Are individual meteorites heavier now then they have been in the past?
- Nope, although there are a couple of years where some really giant ones hit (assuming that the data is correct(could be incorrect entry, more data bais))


* Are Meteorite Landings equally distributed worldwide?
- Yes


-Reasons for discrepancies could be:
    some countries are better able to record meteorites in a percise way
    data collecting bias
    data accuracy (don't forget about thoes entries containing null values that were discarded)

<br><br><br><br><br><br>
***************************************************************
***************************************************************
***************************************************************

* Are the frequency of all meteorite landings equally distributed?

* Are the meteorites masses the same size on average now as they have been in the past?
  - Are meteorites heavier now then they have been in the past?
  >- mass = (kg)
  >- now = (last 50 years)
  >- past = (entire dataset)

* Are the geographical locations of Meteorite Landings equally distributed worldwide?

***************************************************************
***************************************************************
***************************************************************
<br><br><br><br><br><br><br>

# <center>Final Todo list:</center>

Currently working on:
* conclusion
* update readme to include world_map.py(bokeh) information and source credit
* pep8 everything
* more informative comments to explain all of the pieces    
