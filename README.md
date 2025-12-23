#  City Infrastructure Dashboard

A web-based Smart City dashboard that dynamically visualizes city infrastructure locations on an interactive map using Flask, GeoJSON, and Leaflet.js.
This project demonstrates how server-side geographic data can be converted into GeoJSON and rendered dynamically on a client-side map without using any GIS GUI tools.

# Project Objective

To build a dynamic map dashboard that fetches infrastructure data from a server and converts it into GeoJSON
Displays it interactively using Leaflet.js

This approach avoids static maps and manual markers, ensuring scalability and real-time updates.


# GeoJSON is a geographic data format based on JSON that is specifically designed to represent:

# Leaflet.js is a lightweight JavaScript library for interactive maps.

Leaflet uses a layer-based architecture:

Tile Layer - Map background

GeoJSON Layer - Infrastructure markers

Marker / CircleMarker Layers - Individual points

This project dynamically adds and removes GeoJSON layers, enabling real-time updates.

# Technical requirements :
Backend - Flask
Frontend - Html
Data Source - CSV file

A CSV file containing infrastructure data:

Name,Type,Lat,Lon

# API Endpoint

GET

/api/locations

Functionality:

Reads CSV file

Converts rows into GeoJSON Features

Returns a GeoJSON FeatureCollection

CSV - GeoJSON Logic

Each row becomes a GeoJSON Feature

Latitude & Longitude form the Point geometry

Name and Type are stored as properties

Frontend (HTML + JavaScript)
Map Initialization

Centered on Delhi

Uses OpenStreetMap tiles

Default zoom: 12

Dynamic Data Fetching

JavaScript fetches data from /api/locations

Parses GeoJSON response

Uses L.geoJSON() to plot markers automatically

Marker Customization

Circle markers

Different colors based on infrastructure type

Interactive popups showing:

Name

Type

Coordinates

Refresh Button

Allows reloading updated server data without refreshing the page.

# Data Flow
CSV - Flask - GeoJSON - HTTP Request - Leaflet - Map Visualization


# Install Dependencies
pip install -r requirements.txt

# Run the Flask Server
python app.py

# Open in Browser
http://127.0.0.1:5000

# Expected Output

Interactive map with infrastructure markers

Color-coded locations

Popups with detailed information

Dynamic updates via API

# Key Learnings

Converting tabular data into GeoJSON

Using REST APIs for geographic data

Layer-based rendering with Leaflet.js

Dynamic, scalable map dashboards

Conclusion

This project successfully demonstrates a Smart City Infrastructure Dashboard that meets all technical and conceptual requirements of Track B. The solution is lightweight, scalable, and fully dynamic — suitable for real-world smart city applications.