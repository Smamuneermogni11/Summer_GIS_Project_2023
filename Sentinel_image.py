import requests
from PIL import Image

# WMS URL
wms_url = "https://services.sentinel-hub.com/ogc/wms/9b1b49e6-1f7c-4947-a853-3d481601a66b"

# WMS parameters
params = {
    "SERVICE": "WMS",
    "REQUEST": "GetMap",
    "SHOWLOGO": "false",
    "VERSION": "1.3.0",
    "LAYERS": "NDVI",
    "MAXCC": "20",
    "WIDTH": "100",
    "HEIGHT": "100",
    "CRS": "EPSG:4326",
    "BBOX": "-118.9519,33.7056,-118.1553,34.3373",
    "TIME": "2020-01/2020-02",
    "FORMAT": "image/jpeg"
}

# Send WMS request
response = requests.get(wms_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Save the JPEG image to a file
    output_file = r"C:\Muneer\world3.jpg"
    with open(output_file, 'wb') as file:
        file.write(response.content)

    print(f"JPEG image exported to {output_file}")

    # Optionally, you can open and display the image
    image = Image.open(output_file)
    image.show()

else:
    print("Error: Failed to retrieve data from the WMS server.")