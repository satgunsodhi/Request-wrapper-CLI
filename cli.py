import argparse
import json
import requests
from urllib.parse import urlparse

def saveFile(response):
    try:
        response_data = response.json()
        with open("response.json", "w") as file:
            json.dump(response_data, file, indent=4)
        print("Success! Stored at ./response.json")
    except json.JSONDecodeError:
        print("Response is not in JSON format")
        with open("response.txt", "w") as file:
            file.write(response.text)
        print("Success! Stored at ./response.txt")

def validate_url(url):
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        url = 'http://' + url
    try:
        requests.head(url)
        return url
    except requests.exceptions.RequestException:
        print(f"Invalid URL: {url}")
        exit(1)
            
def main():
    print("Welcome to requester CLI!")
    parser = argparse.ArgumentParser(description="Process command line inputs.")
    parser.add_argument('command', choices=['/get', '/post', '/put', '/delete'], help="The command to execute: /get, /post, /put, /delete")
    parser.add_argument('url', help="The URL to send the request to")
    parser.add_argument('data', nargs='?', help="The JSON data for PUT requests")
    args = parser.parse_args()

    command = args.command.lower()
    url = (args.url)

    headers = {
        'Content-Type': 'application/json'
    }
    
    if command == "/get":
        try:
            response = requests.get(url, headers=headers)
            saveFile(response)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred! {e}")
    
    elif command == "/post":
        with open(args.data, 'r') as file:
            data = json.load(file)

        if not args.data:
            print("Error: Missing JSON data for POST request.")
            print('Usage: script.py /post <URL> "<JSON_DATA>"')
            return
        
        try:
            response = requests.post(url, json=data, headers=headers)
            saveFile(response)
        except json.JSONDecodeError:
            print("Invalid JSON format for the request body.")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

    elif command == "/put":
        with open(args.data, 'r') as file:
            data = json.load(file)
    
        if not args.data:
            print("Error: Missing JSON data for PUT request.")
            print('Usage: script.py /put <URL> "<JSON_DATA>"')
            return
        try:
            response = requests.put(url, json=data, headers=headers)
            saveFile(response)
        except json.JSONDecodeError:
            print("Invalid JSON format for the request body.")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
        
    
    elif command == "/delete":
        try:
            response = requests.delete(url, headers=headers)
            saveFile(response)
        except requests.exceptions.RequestException:
            print("An error occured! {e}")

if __name__ == "__main__":
    main()