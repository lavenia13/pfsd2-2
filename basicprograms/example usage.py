import urllib.request, urllib.parse, urllib.error
import json

# Input the location
location = input('Enter location: ')

# Encode the location for the URL
url_encoded_location = urllib.parse.urlencode({'q': location})

# Construct the API URL
api_url = "http://py4e-data.dr-chuck.net/opengeo?" + url_encoded_location

# Retrieve JSON data from the API
json_data = urllib.request.urlopen(api_url).read()

# Parse the JSON data
data = json.loads(json_data)

# Extract the plus_code from the nested 'properties'
properties = data.get('features', [{}])[0].get('properties', {})
plus_code = properties.get('plus_code', 'Not found')

# Print the plus_code
print('Plus code:', plus_code)
