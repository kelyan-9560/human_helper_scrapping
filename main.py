import requests
from bs4 import BeautifulSoup

#url = 'http://localhost:4200/camps'
url = 'https://meteo.francetvinfo.fr/france/ile-de-france/bobigny_93000'
response = requests.get(url)

if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser')
    tempSoiree = soup.find('ul', {'class': 'forecast-details'}).find('li', {'class': 'evening'}).find('div', {'class': 'forecast big'}).find('span', {'class': 'temparature'})

    print(tempSoiree.)


else:
    print(response)

