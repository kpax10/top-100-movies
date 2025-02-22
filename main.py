import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

URL = 'https://www.imdb.com/list/ls055592025/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

response = requests.get(url=URL, headers=headers)
movies_webpage = response.text

soup = BeautifulSoup(movies_webpage, 'html.parser')
movies = soup.find_all('h3', class_='ipc-title__text')
movie_ranking = []
movie_title = []

for movie_tag in movies:
    ranking = movie_tag.get_text().split()[0].replace('.', ')')
    movie_ranking.append(ranking)
    title = movie_tag.get_text().split(' ', 1)[1]
    movie_title.append(title)
    print(ranking, title)

df = pd.DataFrame([movie_ranking]) # work on this
df.to_csv('movies.csv', mode='w')
