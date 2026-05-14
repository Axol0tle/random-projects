git config --global user.email "landon7071@gmail.com"
git config --global user.name "Axol0tle"

touch scraper.py
pip install requests
import requests

response = requests.get(
    url="https://en.wikipedia.org/wiki/Web_scraping","
)
print(response.status_code)

python3 scraper.py
200 

pip install beautifulsoup4
