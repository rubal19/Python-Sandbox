import requests
from bs4 import BeautifulSoup

url = 'https://www.willhaben.at/iad/immobilien/eigentumswohnung/steiermark'

response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")


    