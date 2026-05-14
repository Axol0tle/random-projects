import requests
from bs4 import BeautifulSoup

# 1. Create a fake "User-Agent" so the website thinks you are a normal browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# 2. Add the headers to your request
response = requests.get(
    url="https://en.wikipedia.org/wiki/Web_scraping",
    headers=headers
)

# 3. Print the status code (200 means success, 403 means you are blocked!)
print(f"Status Code: {response.status_code}") 

soup = BeautifulSoup(response.content, 'html.parser')

title = soup.find(id="firstHeading")

# 4. Check if the title was actually found before trying to print it
if title:
    print(title.text)
else:
    print("Could not find the title! The page structure might be different.")