import folium
import json

# Load GeoJSON data
with open("data/california_airfields.geojson") as f:
    airfields = json.load(f)

# Base map centered over California
m = folium.Map(location=[36.5, -119.5], zoom_start=6, tiles="CartoDB positron")

# Add GeoJSON with styled markers, tooltips, and popups
folium.GeoJson(
    airfields,
    name="California Airfields",
    tooltip=folium.GeoJsonTooltip(
        fields=["Airport_Name", "ICAO"],
        aliases=["Airport:", "ICAO Code:"],
        sticky=False
    ),
    popup=folium.GeoJsonPopup(
        fields=["Procedure_Title", "Design_Criteria"],
        aliases=["Procedure:", "Design Criteria:"],
        max_width="300"
    ),
    style_function=lambda feature: {
        "color": "#0073e6",
        "weight": 2,
        "fillOpacity": 0.6
    }
).add_to(m)

folium.LayerControl().add_to(m)
m.save("california_airfields_map.html")
