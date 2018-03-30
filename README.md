
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

4) The terminal will give you further information on script, create an sqlite database and output graphs to `./graphs`

<br></br>

---
## <center> Data Set:

This data set was created by the Meteoritical Society and it contains information on all known meteorite landings. The information is from October 29, 2015 and contains 45.7K rows(Before null values are removed). After processing the dataset and deleting lots of NULL values, it ended up closer to 38k entries https://data.nasa.gov/Space-Science/Meteorite-Landings/ak9y-cwf9

There is csv file contained in this repo for convience, however it is not modified at any point.  The idea was to load it into a sqlite database and manipulate the data from there.  That way, as data is update in the csv file, the corosponding sqlite database and graphs would also update correctly.

<br></br>

# <center>Project Requirements

#### 1)  Problem that I am analyzing: 

    
* Are the frequency of meteorite landings equally distributed?

* Are the meteorites masses the same size on average now as they have been in the past?
  - Are meteorites heavier now then they have been in the past?
  >- mass = (kg)
  >- now = (last 50 years)
  >- past = (entire dataset)

* Are the geographical locations of Meteorite Landings equally distributed worldwide?


---
#### 2)  Include SQL database where your data will be stored and manipulated.  You need to include a script that sets up/creates your database
AND
#### 3)  You must include a Python script used to fetch data from a data source and load it into your SQL database
---
* This snippet of code creates a meteo.db sqlite database opens the csv file in read mode and passes it to a csv reader.  This snippit is located in `create_sql.py`:

```python
        sql = sqlite3.connect('meteo.db')
        cur = sql.cursor()
        csv_file = open('Meteorite_Landings.csv','r', errors='ignore')
        next(csv_file, None)
        reader = csv.reader(csv_file)

```

* This snippet of code creates the main table (meteorite_data) from the csv file.  There are also several other smaller tables created from the information in this table like (count and total_mass_kg). This snippet is located in `create_sql.py`:

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
#### 4) You must include a Python script to retrieve the data from your SQL database into a Python object
---

* This is primarily located in the `graphs.py` file that is included.  Data is taken from the SQL database and loaded into a pandas python object (dataframe) to be further processed (cleaned) and passed to matplotlib and bokeh for graphing

```python
        conn = sqlite3.connect('meteo.db')
        meteorites = pd.read_sql_query('SELECT year, count FROM meteorite_frequency ORDER BY year DESC;', conn)
        conn.close()

        last_50_years = meteorites[0:50]
```

<br></br>
#### 5)  You must include a Python script to modify your data so as to prepare it for visualization

---
* This happens in several places throughout the project.  The first time is in `create_sql.py` (specifically in the function `clean_empty_values()`) and is also done through sqlite querries to remove rows with null values so the csv data can be succesfully passed to the sqlite database (meteo.db)
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

* This is to get rid of a lingering incorrect year from the future(likely an entry error)

```python
        meteorites = meteorites[meteorites.year_only <= 2018]

```
<br></br>
#### 6)  Visualize the results of your analysis using Matplotlib, Seaborn, Bokeh or another Python Data Visualization library. Your results cannot be a plaintext representation and you are encouraged to explore a visualization approach that clearly supports a conclusion/result of the analysis of your data.
---
* Multiple graphs are made using matplotlib, they are sent to the /graphs directory when the script is ran.  Pre ran copies of all graphs are located in the /graph folder on github, but they are simply the last generated output since my last git push.  The folder must exist for the script to run, but none of the graphs are necessary, they are generated dynamically from the csv file.

---
## Matplot lib Graphs
---
This is the last output generated by `ProjectRUN.py`.  These files are generated when the script runs, if there are files with the same name, they will be overwritten.

## <center> Frequency per year

<div>
<center>

![Bar graph of the frequency that meteorites have hit the earth in the last 50 years](/graphs/frequency_bar_last_50.png "Bar graph of the frequency that meteorites have hit the earth in the last 50 years")

![Line graph of the frequency that meteorites have hit the earth in the last 50 years](/graphs/frequency_line_last_50.png "Line graph of the frequency that meteorites have hit the earth in the last 50 years")

![Bar graph of the frequency that meteorite have hit the earth in the entire data set](/graphs/frequency_bar.png "Bar graph of the frequency that meteorite have hit the earth in the entire data set")

![Line graph of the frequency that meteorite have hit the earth in the entire data set](/graphs/frequency_line.png "Line graph of the frequency that meteorite have hit the earth in the entire data set")

Maximum mass per year

![Bar graph of the maximum mass of meteorites per year for the last 50 years](/graphs/year_max_mass_bar_last_50.png "Bar graph of the maximum mass of meteorites per year for the last 50 years")

![Line graph of the maximum mass of meteorites per year for the last 50 years](/graphs/year_max_mass_line_last_50.png "Line graph of the maximum mass of meteorites per year for the last 50 years")


![Bar graph of the maximum mass of meteorites per year for the entire data set](/graphs/year_max_mass_bar.png "Bar graph of the maximum mass of meteorites per year for the entire data set")

![Line graph of the maximum mass of meteorites per year for the entire data set](/graphs/year_max_mass_line.png "Line graph of the maximum mass of meteorites per year for the entire data set")

</center>
</div>

### Bokeh 
Visualizations will pop out at the end when you run when you run `ProjectRUN.py`

They include:
* `world_map_json()` - This a uses patches to map country shapes (using json data) onto a graph which can then be used to plot latitude and longitude.  This script is a modified version of the Treehouse Python course 'Data Visualization with Bokeh' in the video 'Plotting the World' and was very useful.  The patches json data was created by Johan Sundstrom and can be located at https://github.com/johan/world.geo.json.

* `world_map_google()` - This uses the google maps API to graph all of the meteorite landings on the world.  I set the starting geolocation at my location, but in the future I plan to update this map to start at the users geolocation.

# <center> Conclusion

<center>

![Line of best fit](/graphs/frequency_line_last_50_lob.png "Line of best fit overtop of frequency / time")

</center>

This is by no means a perfect representation of the data, but appears to support the theory that most data falls within a reasonable deviation.

---

### Is the frequency of meteorite landings equally distributed?
>> The data is mixed, It appears that we have had an explosion of records over the last 50 years in the data set but this doesn't necessarily translate to having more meteorite landings.  

>> Within the last 50 years of the data set there appears to be an upward trend in the frequency meteorite landings are recorded, but there are also lots of explanations that could explain these trends.

>> As for the entire data set, advances in telescopes and general technology would explain why there would be so many more records in the past 50 years.  

>> As for recent history, the vast majority of the data falls within one standard deviation of the median which leads me to believe that meteorites are likely falling at a similar rate as always.  

### Are the meteorites masses the same size as they have been in the past?

>> Other than a couple of outliers and plenty of reasons why we record more data now than in the past, it does not appear that meteorites are heavier now than they used to be.  If there are any trends, it likely has more to do with record errors, data entry or just sheer outliers.

### Are the geographical locations of Meteorite Landings equally distributed worldwide?
>> Not really, but they made for a pretty fun google map project.  One of my favorite parts of this project was learning to use the google maps API with bokeh.

I hope you have enjoyed looking at my project as I did working on it.  It was really interesting to work through the puzzle pieces that eventually became this final project.

---

#### Reasons everything could be wrong:

Reasons for discrepancies could be:
- some countries are better able to record meteorites in a precise way
- data collecting bias
- data accuracy (don't forget about those entries containing null values that were discarded)

#### What I have learned and where does this project go from here?

There are lots of ways that this project could be improved upon moving forward.  This script uses several different libraries to accomplish similar things, I did this on purpose; to dabble around in the current python environment to learn common solutions to frequent problems.  I really enjoyed learning to use the pandas library, I particularly found the dataframe object to be useful in many ways.  I also found it very interesting from a work flow perspective to take a csv file, read it and load it into a sqlite db without manipulating it, and then working on various problems within the sqlite database.  It felt pretty strange to send SQL queries through python at first, but then really started to make sense as I progressed through the project.

From here I would like to make a user interface for this program along with more user input, including their geolocation.  I will expand on my google maps bokeh visualization as well as general code and library reduction.


---
<div style="text-align: right">
This project is under MIT license
</div>