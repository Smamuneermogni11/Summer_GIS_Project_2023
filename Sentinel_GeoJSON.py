import requests
import json

# WMS URL
wms_url = "https://services.sentinel-hub.com/ogc/wms/9b1b49e6-1f7c-4947-a853-3d481601a66b?SERVICE=WMS&REQUEST=GetMap&SHOWLOGO=false&VERSION=1.3.0&LAYERS=SWBM&MAXCC=20&WIDTH=640&HEIGHT=640&CRS=EPSG:4326&BBOX=38.481634,-122.503351,38.533838,-122.42798&FORMAT=application/json"

# WMS parameters
params = {
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "COLOR_HEX": "FFFFFF",
        "ID": 0
      },
      "geometry": {
        "type": "MultiPolygon",
        "crs": {
            "type": "name",
            "properties": {
                "name": "urn:ogc:def:crs:OGC::CRS84"
            }
        },
        "coordinates": [[[
            [-122.503351, 38.51637],
            [-122.478057, 38.533838],
            [-122.42798, 38.499095],
            [-122.454379, 38.481634],
            ...
        ]]]
      }
    },
    ...
  ]
}

# Send WMS request
response = requests.get(wms_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Load the GeoJSON data
    geojson_data = response.json()

    # Save GeoJSON data to a file
    output_file = r"C:\Muneer\water.geojson"
    with open(output_file, 'w') as file:
        json.dump(geojson_data, file)

    print(f"GeoJSON data exported to {output_file}")

else:
    print("Error: Failed to retrieve data from the WMS server.")