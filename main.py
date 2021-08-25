import requests
from bs4 import BeautifulSoup


# url = 'http://localhost:4200/camps'
# url = 'https://meteo.francetvinfo.fr/france/ile-de-france/bobigny_93000'


def print_data(datas, hour, temp):
    if hour is not None :
        if temp is not None:
            datas[hour] = temp



def write_in_file(filename, datas):
    with open(filename, 'w') as file:
        for key, value in datas.items():
            file.write('[' + key.text + ':' + value.text + ']' + '\n')




def meteo(ville):
    ville.lower()

    url = 'https://www.xn--mto-bmab.fr/' + ville
    response = requests.get(url)

    datas = {}

    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')

        liS = soup.findAll('li')
        tabHours = []
        tabTemps = []
        for li in liS:
            hour = li.find('h4')
            tabHours.append(hour)

            temp = li.find('dd', {'class': 'temp'})
            tabTemps.append(temp)

            print_data(datas, hour, temp)

        write_in_file('data.txt', datas)

        print(tabHours)
        print(tabTemps)
        print(datas)

    else:
        print(response)


test = 'ermont'
meteo(test)
