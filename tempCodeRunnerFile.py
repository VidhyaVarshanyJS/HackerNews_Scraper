import requests
from bs4 import BeautifulSoup

res = requests('https://news.ycombinator.com')
print(res)
