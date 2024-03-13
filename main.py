import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com"
req = requests.get(url)

soup = BeautifulSoup(req.text, "html.parser")

links = soup.select(".titleline > a")
subtexts = soup.select('.subtext')

print(subtexts)