# Airfield GIS Data Integration – California Edition

I am an aeronautical analyst with experience in aviation operations, predictive modeling, and spatial data strategy. This repository documents the integration of ICAO-based procedural metadata into geospatial formats across major California airports.

During the initial phase, I used Python and open-source geospatial libraries to convert airfield attributes—including coordinates, procedure titles, and design criteria—into a standardized GeoJSON dataset. The process was executed in a cloud-native notebook environment and includes an interactive visualization rendered in Folium.

The methods applied here support further integration of navigational systems, holding patterns, lighting systems, and procedural overlays. A full expansion plan is outlined below.

## Contents
- `california_airfields.geojson`: Spatial data for KLAX, KSFO, and KSAN  
- Scripts for geospatial conversion and interactive rendering  
- Folium-based map visualization (Google Colab)

## Tools Used
- Python (GeoPandas, Folium, Pandas, Shapely)  
- Google Colab  
- GitHub

## Expansion Plans
- Add procedural geometry (missed approach tracks, holding patterns)  
- Integrate regulatory metadata (PBN notes, communication frequencies)  
- Automate extraction from Host graphics and Supplement PDFs
