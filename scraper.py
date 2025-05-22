"""
I am searching for a "Car Cover" on OLX - using www.olx.in/items/q-car-cover; write a python program that gives me the search results in a file. Place code in Github & share the link.
"""

import requests
from bs4 import BeautifulSoup

url = "https://www.olx.in/items/q-car-cover"
headers = {"User-Agent": "Mozilla/5.0"}
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, "html.parser")
results = [i.text for i in soup.select("a.EIR5N")]
with open("olx_car_covers.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(results))
