import requests
from bs4 import BeautifulSoup

ville = 'paris'
filename = 'data.txt'


def check_data(datas, hour, temp):
    if hour is not None:
        if temp is not None:
            datas[hour] = temp


def header():
    with open(filename, 'w') as file:
        file.write('---------------')
        file.write('Informations concernant les températures de nuit de la ville de : ' + ville)
        file.write('---------------' + '\n')


def find_key(v, datas):
    for k, val in datas.items():
        if v == val:
            return k
    return "Clé n'existe pas"


def extreme_cold(datas):
    with open(filename, 'a') as file:
        file.write('--------------------------------' + '\n')
        file.write('!!! Opération Grand Froid !!!' + '\n')

        for key, value in datas.items():
            tempMin = min(value)

        file.write('Pique de froid : ' + tempMin + '\n')
        file.write('Heure : ' + find_key(tempMin, datas) + '\n')
        file.write('--------------------------------' + '\n')


def write_in_file(datas):
    with open(filename, 'a') as file:
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

            check_data(datas, hour, temp)

        header()

        for value in datas.values():
            if value is not None:
                valueSplit = value.text.replace('°', '')
                if int(valueSplit) < 5:
                    extreme_cold(datas)
        write_in_file(datas)

        print(tabHours)
        print(tabTemps)
        print(datas)

    else:
        print(response)


meteo(ville)
