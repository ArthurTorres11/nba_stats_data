from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

load_dotenv()

def coletar_dados_temporada(ano):
    url = f"https://www.basketball-reference.com/leagues/NBA_{ano}_totals.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', {'id': 'totals_stats'})
    rows = table.find_all('tr')

    header = [th.text for th in rows[0].find_all('th')][1:]

    data = []
    for row in rows[1:]:
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)

    df = pd.DataFrame(data, columns=header)
    df['Ano'] = ano

    return df

dados_historicos = pd.concat([coletar_dados_temporada(ano) for ano in range(2020, 2026)])
dados_historicos.to_csv('data/raw/dados_historico.csv', index=False)


def coletar_dados_times(ano):
    url = f"https://www.basketball-reference.com/leagues/NBA_{ano}_standings.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', {'id': 'confs_standings_E'})
    rows = table.find_all('tr')


    header = [th.text for th in rows[0].find_all('th')][1:]
    data = []
    for row in rows[1:]:
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)

    df = pd.DataFrame(data, columns=header)
    df['Ano'] = ano
    return df

dados_times = pd.concat([coletar_dados_times(ano) for ano in range(2020, 2026)])
dados_times.to_csv('data/raw/dados_times.csv', index=False)

def coletar_dados_lesao(ano):
    url = f"https://www.basketball-reference.com/leagues/NBA_{ano}_injuries.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', {'id': 'injuries'})
    rows = table.find_all('tr')

    header = [th.text for th in rows[0].find_all('th')][1:]
    data = []
    for row in rows[1:]:
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)

    df = pd.DataFrame(data, columns=header)
    df['Ano'] = ano
    return df

dados_lesoes = pd.concat([coletar_dados_lesao(ano) for ano in range(2020, 2026)])
dados_lesoes.to_csv('data/raw/dados_lesoes_nba.csv', index=False)