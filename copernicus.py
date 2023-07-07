import cdsapi

# Create a CDS API client
c = cdsapi.Client(url="https://cds.climate.copernicus.eu/api/v2", key="210166:3c88417b-3015-4b7c-b2af-b68ed065f332")

# Define the request parameters
request = {
    'variable': [
        '2m_dewpoint_temperature', '2m_temperature', 'skin_temperature',
        'soil_temperature_level_1', 'soil_temperature_level_2', 'soil_temperature_level_3',
        'soil_temperature_level_4',
    ],
    'year': '2023',
    'month': '07',
    'day': '01',
    'format': 'netcdf',
    'time': [
        '00:00', '01:00', '02:00',
        '03:00', '04:00', '05:00',
        '06:00', '07:00', '08:00',
        '09:00', '10:00', '11:00',
        '12:00', '13:00', '14:00',
        '15:00', '16:00', '17:00',
        '18:00', '19:00', '20:00',
        '21:00', '22:00', '23:00',
    ],
}

# Send the request and download the data
c.retrieve('reanalysis-era5-land', request, 'C:/Face_Recognition/Temperature.nc')
