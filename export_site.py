import os
import sys
import requests

def save_website(url, folder="saved_sites"):
    os.makedirs(folder, exist_ok=True)  # Ensure folder exists
    filename = os.path.join(folder, url.replace("https://", "").replace("http://", "").replace("/", "_") + ".html")

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        with open(filename, "w", encoding="utf-8") as file:
            file.write(response.text)
        print(f"Saved: {filename}")
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fetch_site.py <URL>")
        sys.exit(1)
    
    save_website(sys.argv[1])

