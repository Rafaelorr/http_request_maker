import requests
import json
import re

# api-endpoint
url = input("Typ het API endpoint URL: ")

pattern = r'https?://\S+|www\.\S+'
if not re.findall(pattern,url):
    print("Ongeldige URL. Zorg ervoor dat de URL begint met http:// of https://")
    url = input("Typ het API endpoint URL: ")

while True:
    param_file = input("Typ de bestandsnaam van de parameters (bijv. params.json): ")
    if param_file.strip():
        break
    else:
        print("Type een geldige bestandsnaam.")

with open(param_file, "r") as f:
    params = json.load(f)

# sending get request and saving the response as response object
r = requests.get(url = url, params = params)

# extracting data in json format
data = r.json()

print(data)