import requests
import json
import re

def is_valid(json_string):
    print("JSON String:", json_string)
    try:
        json.loads(json_string)
        print("  Is valid?: True")
    except ValueError:
        print("  Is valid?: False")
        return None

# api-endpoint
while True:
    url = input("Typ het API endpoint URL: ")
    pattern = r'https?://\S+|www\.\S+'
    if re.findall(pattern,url):
        break
    print("Ongeldige URL. Zorg ervoor dat de URL begint met http:// of https://")
    url = input("Typ het API endpoint URL: ")

while True:
    param_file = input("Typ de bestandsnaam van de parameters (bijv. params.json): ")
    if param_file.strip() and is_valid(param_file):
        break
    print("Type een geldig json bestandsnaam.")

with open(param_file, "r") as f:
    params = json.load(f)

# sending get request and saving the response as response object
r = requests.get(url = url, params = params)

# extracting data in json format
data = r.json()

print(data)