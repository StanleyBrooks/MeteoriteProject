from bokeh.io import output_file, show
from bokeh.plotting import figure

from bokeh.io import output_file, show
from bokeh.models import (GMapPlot, GMapOptions, ColumnDataSource, Circle, Range1d, PanTool, WheelZoomTool, BoxSelectTool)

import numpy as np
import pandas as pd
import json
import requests
import sqlite3


def world_maps():

    """Collect sqlite data and put it into a pandas dataframe for additional cleaning and graphing"""
    #use pandas to retrieve sqlite tables
    conn = sqlite3.connect('meteo.db')
    meteorites_geo = pd.read_sql_query('SELECT reclat, reclong FROM meteorite_data;', conn)
    conn.close()

    #remove NA values
    meteorites_geo = meteorites_geo.dropna()

    #Use pandas to convert strings into numbers(floats)
    meteorites_geo['reclong'] = meteorites_geo['reclong'].astype(float)
    meteorites_geo['reclat'] = meteorites_geo['reclat'].astype(float)

    output_file("./graphs/world-map.html", title="Worldwide Meteorite Landings")

    #This section uses Bokeh patches and json data of country boundries to map the world.  This code
    # is a modified version of a project worked on by Ken Alger in the treehouse.com tutorial 
    # 'Data Visualization with Bokeh' in the video 'Plotting the World'.  The map of the world
    # comes from Johan Sundström who has a github at https://github.com/johan/world.geo.json

    def world_map_json():
        url = 'https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json'
        r = requests.get(url)
        json_data = r.json()


        def get_coordinates(features):
            depth = lambda L: isinstance(L, list) and max(map(depth, L))+1
            longitudes = []
            latitudes = []

            for feature in json_data['features']:
                coordinates = feature['geometry']['coordinates']
                number_dimensions = depth(coordinates)
                # one border
                if number_dimensions == 3:

                    points = np.array(coordinates[0], 'f')
                    longitudes.append(points[:, 0])
                    latitudes.append(points[:, 1])
                    # several borders
                else:
                    for shape in coordinates:
                        points = np.array(shape[0], 'f')
                        longitudes.append(points[:, 0])
                        latitudes.append(points[:, 1])
            return longitudes, latitudes

        lats, longs = get_coordinates(json_data['features'])

        #took off hover for now due to performance issues
        TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

        #make graph that is bound by Geographic Coordinates
        world_map_plot = figure(plot_width=900,
                                plot_height=600,
                                title="Meteorite Landings",
                                tools=TOOLS,
                                x_range=(-180, 180),
                                y_range=(-90, 90))


        #This applies the geometic shapes to a lat,long grid
        world_map_plot.patches(lats, longs, fill_color="#F1EEF6", fill_alpha=0.7, line_width=2)

        #Meteorite landings data mapped over the top of the world patch in red
        world_map_plot.scatter(meteorites_geo['reclong'], meteorites_geo['reclat'], fill_color="#FF0000", fill_alpha=1, line_width=.5)

        #Show the data
        show(world_map_plot)


    def world_map_google():

        """Collect sqlite data and put it into a pandas dataframe for additional cleaning and graphing"""
        #use pandas to retrieve sqlite tables
        conn = sqlite3.connect('meteo.db')
        meteorites_geo = pd.read_sql_query('SELECT reclat, reclong FROM meteorite_data;', conn)
        conn.close()

        #remove NA values
        meteorites_geo = meteorites_geo.dropna()

        #Use pandas to convert strings into numbers(floats)
        meteorites_geo['reclong'] = meteorites_geo['reclong'].astype(float)
        meteorites_geo['reclat'] = meteorites_geo['reclat'].astype(float)

        output_file("./graphs/world-map.html", title="Worldwide Meteorite Landings")

        #This is my current location, would like to replace this with users current GeoLocation in the future
        map_options = GMapOptions(lat=38.229660599999995, lng=-85.7405836, map_type="terrain", zoom=6)

        world_map_plot = GMapPlot(x_range=Range1d(), y_range=Range1d(), map_options=map_options)
        world_map_plot.title.text = "Meteorite Landing Locations"

        # For GMaps to function, Google requires you obtain and enable an API key:
        #
        #     https://developers.google.com/maps/documentation/javascript/get-api-key
        #
        # Replace the value below with your personal API key:
        world_map_plot.api_key = "AIzaSyCTH9aO_DdSi_OxiZtuj7xie8-5kHzjjeg"

        data=dict(lat=meteorites_geo['reclat'],lon=meteorites_geo['reclong'])
        
        source = ColumnDataSource(data)

        circle = Circle(x="lon", y="lat", size=5, fill_color="red", fill_alpha=0.9, line_color=None)
        world_map_plot.add_glyph(source, circle)

        world_map_plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())
        output_file("./graphs/google_world_map.html")
        show(world_map_plot)


    world_map_json()
    world_map_google()