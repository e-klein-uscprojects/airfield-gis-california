# Usage Guide – Airfield GIS Data Integration

I am an aeronautical analyst with a background in aviation operations and geospatial strategy. This repository reflects my efforts to convert ICAO-based procedural metadata into an interactive mapping environment designed to support airspace modeling and regional planning across California airports.

Over the course of this work, I implemented Python-based spatial tools to structure data for KLAX, KSFO, and KSAN, drawing from publicly available procedural diagrams and design criteria. Using Folium and GeoPandas, I was able to render location-based overlays that expose runway procedures, metadata, and ICAO tagging in an easily navigable format.

Those wishing to replicate or review this visualization may begin by accessing the files hosted here. I invite users to download the repository, open the associated scripts or notebooks, and execute the rendering functions. The resulting map includes embedded metadata popups and customizable visual layers.

The current package relies on Python 3.9 or greater, and assumes use of the following libraries: `geopandas`, `pandas`, `folium`, and `shapely`. File contents are organized into dedicated folders and include:

- `/data`: All GeoJSON content used in the initial visualization
- `/scripts`: Python-based map rendering modules
- `/notebooks`: Preview notebooks available for adaptation or cloud execution
- `/README.md`: Project overview, background, and technical structure

This project remains open to future expansion and collaborative input. I appreciate your time and interest in reviewing this material.
