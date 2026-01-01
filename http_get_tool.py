import requests
import json
import re
import os

def is_valid_json_string(json_string):
    """Controleer of een string geldig JSON is."""
    try:
        json.loads(json_string)
        return True
    except ValueError:
        return False

def get_valid_url():
    """Vraag de gebruiker herhaaldelijk om een geldige URL."""
    pattern = r'^https?://\S+'
    while True:
        url = input("Typ het API endpoint URL: ").strip()
        if re.match(pattern, url):
            return url
        print("Ongeldige URL. Zorg ervoor dat de URL begint met http:// of https://")

def get_valid_param_file():
    """Vraag de gebruiker herhaaldelijk om een geldig JSON-bestand met parameters."""
    while True:
        param_file = input("Typ de bestandsnaam van de parameters (bijv. params.json): ").strip()
        if not param_file:
            print("Voer een bestandsnaam in.")
            continue
        if not os.path.isfile(param_file):
            print(f"Bestand '{param_file}' bestaat niet. Probeer het opnieuw.")
            continue
        try:
            with open(param_file, 'r') as f:
                params = json.load(f)
            return params
        except json.JSONDecodeError:
            print("Het bestand bevat geen geldig JSON. Probeer een ander bestand.")
        except Exception as e:
            print(f"Fout bij het lezen van het bestand: {e}")

if __name__ == "__main__":
    url = get_valid_url()
    params = get_valid_param_file()

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Check voor HTTP fouten
        data = response.json()
        json_str = json.dumps(data, indent=4)
        with open("response.json", "w") as f:
            f.write(json_str)
    except requests.exceptions.RequestException as e:
        print(f"Fout bij het maken van de API-aanroep: {e}")
    except json.JSONDecodeError:
        print("De response van de API is geen geldige JSON.")