from bs4 import BeautifulSoup
import requests as rq
import pandas as pd
from openpyxl.workbook import Workbook

year = int(input("Você gostaria de verificar os dados da copa do mundo de que ano? "))

def get_matches(year):
    web = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'
    request = rq.get(web)
    content = request.text
    soup = BeautifulSoup(content, 'lxml')
    matches = soup.find_all('div', class_='footballbox')

    home = []
    score = []
    away = []

    for match in matches:
        home.append(match.find('th', class_='fhome').get_text())
        score.append(match.find('th', class_='fscore').get_text())
        away.append(match.find('th', class_='faway').get_text())
    
    dict_match = {'home' : home, 'score' : score, 'away' : away}
    df_match = pd.DataFrame(dict_match)
    df_match['year'] = year

    return df_match

    
world_cup = get_matches(year)

if year < 2022:
    world_cup.to_excel(f'world_cup_{year}.xlsx', index=False)
else:
    world_cup.to_excel("world_cup_2022.xlsx", index=False)    


print(world_cup)