import requests
import json
import re
import os

def is_valid_json_string(json_string) -> bool:
    """Controleer of een string geldig JSON is."""
    try:
        json.loads(json_string)
        return True
    except ValueError:
        return False

def get_valid_url() -> str:
    """Vraag de gebruiker herhaaldelijk om een geldige URL."""
    pattern = r'^https?://\S+'
    while True:
        url :str = input("Typ het API endpoint URL: ").strip()
        if re.match(pattern, url):
            return url
        print("Ongeldige URL. Zorg ervoor dat de URL begint met http:// of https://")

def get_valid_param_file() -> dict:
    """Vraag de gebruiker herhaaldelijk om een geldig JSON-bestand met parameters."""
    while True:
        param_file :str = "get_config.json"
        if not os.path.isfile(param_file):
            print(f"Bestand '{param_file}' bestaat niet. ")
            continue
        try:
            with open(param_file, 'r') as f:
                params :dict = json.load(f)
            return params
        except json.JSONDecodeError:
            print("Het bestand bevat geen geldig JSON. Probeer een ander bestand.")
        except Exception as e:
            print(f"Fout bij het lezen van het bestand: {e}")

if __name__ == "__main__":
    url :str = get_valid_url()
    params :dict = get_valid_param_file()

    timeout = params.pop("timeout", 5.0)
    allow_redirects = params.pop("allow-redirects",True)
    headers = params.pop("headers",{})


    data :dict = {}

    try:
        response = requests.get(url, timeout=timeout, allow_redirects=allow_redirects,headers=headers, params=params)
        response.raise_for_status()

        # Headers opslaan
        data["headers"] = {
            "Server": response.headers.get("Server"),
            "Date": response.headers.get("Date"),
            "Content-Type": response.headers.get("Content-Type"),
            "Content-Length": response.headers.get("Content-Length"),
            "Connection": response.headers.get("Connection"),
        }

        # Response status info
        data["status"] = {
            "status_code": response.status_code,
            "reason": response.reason,
            "encoding": response.encoding,
            "history": [h.headers for h in response.history]
        }

        # Probeer JSON te parseren
        try:
            json_response = response.json()
            data["json"] = json_response
        except json.JSONDecodeError:
            data["text"] = response.text

        # Alles in output.json opslaan
        with open("output.json", "w") as f:
            json.dump(data, f, indent=4)

        print("Data succesvol opgeslagen in output.json")

    except requests.exceptions.RequestException as e:
        print(f"Fout bij het maken van de API-aanroep: {e}")