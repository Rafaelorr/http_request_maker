#!/usr/bin/env python3
import requests
import json
import re
import os
import argparse
from requests.structures import CaseInsensitiveDict

parser = argparse.ArgumentParser(
                    prog='resp-analyse',
                    description='Dit programma analyseert het HTTP response van een server. Het moet eerst een custom HTTP request maken naar die server.',
                    add_help=True,
                    exit_on_error=False)

parser.add_argument("-u", "--url")
parser.add_argument("-o", "--output")

args = parser.parse_args()

if not args.url:
    exit()

if not args.output:
    print("Er is geen output bestand naam gegeven")
    print("Het output bestand gaat 'output.json' zijn")
    args.output = "output"


def is_valid_json_string(json_string) -> bool:
    """Controleer of een string geldig JSON is."""
    try:
        json.loads(json_string)
        return True
    except ValueError:
        return False

def get_valid_url(args) -> str:
    pattern = r'^https?://\S+'
    url :str = args.url
    if re.match(pattern, url):
        return url
    print("Ongeldige URL. Zorg ervoor dat de URL begint met http:// of https://")
    exit()

def get_valid_param_file() -> dict:
    param_file :str = "get_config.json"
    if not os.path.isfile(param_file):
        print(f"Bestand '{param_file}' bestaat niet. ")
        exit()
    try:
        with open(param_file, 'r') as f:
            params :dict = json.load(f)
        return params
    except json.JSONDecodeError:
        print("Het bestand bevat geen geldig JSON. Probeer een ander bestand.")
    except Exception as e:
        print(f"Fout bij het lezen van het bestand: {e}")

def convert_to_dict(obj):
    if isinstance(obj, CaseInsensitiveDict):
        return {k: convert_to_dict(v) for k, v in obj.items()}
    elif isinstance(obj, dict):
        return {k: convert_to_dict(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_to_dict(item) for item in obj]
    else:
        return obj

if __name__ == "__main__":
    url :str = get_valid_url(args)
    params :dict = get_valid_param_file()

    timeout = params.pop("timeout", 5.0)
    allow_redirects = params.pop("allow-redirects",True)
    headers = params.pop("headers",{})
    cookies = params.pop("cookies",{})


    data :dict = {}

    try:
        response = requests.get(url, timeout=timeout, allow_redirects=allow_redirects,headers=headers, params=params, cookies=cookies)
        response.raise_for_status()

        # Headers opslaan
        data["headers"] = {
            "Server": response.headers.get("Server"),
            "Date": response.headers.get("Date"),
            "Content-Type": response.headers.get("Content-Type"),
            "Content-Length": response.headers.get("Content-Length"),
            "Connection": response.headers.get("Connection"),
            "Set-Cookie": response.headers.get("Set-Cookie")
        }

        # Response status info
        data["status"] = {
            "status_code": response.status_code,
            "reason": response.reason,
            "encoding": response.encoding,
            "history": [h.headers for h in response.history]
        }

        # Cookies
        data["cookies"] = dict(response.cookies)

        # Probeer JSON te parseren
        try:
            json_response = response.json()
            data["json"] = json_response
        except json.JSONDecodeError:
            data["text"] = response.text

        # Alles in output.json opslaan
        with open(f"{args.output}.json", "w") as f:
            json.dump(convert_to_dict(data), f, indent=4)

        print(f"Data succesvol opgeslagen in '{args.output}.json'")

    except requests.exceptions.RequestException as e:
        print(f"Fout bij het maken van de API-aanroep: {e}")