import requests
import json
from bs4 import BeautifulSoup


TITLE =[]
RATING=[]
YEAR=[]
ICON=[]


url = 'https://www.imdb.com/chart/top/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print('Page loaded successfully!\n')
    page_content = response.text
    soup = BeautifulSoup(page_content, 'html.parser')

    content_divs = soup.find_all('div', class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 iALATN cli-title")
    for div in content_divs:
        title = div.find('h3', class_='ipc-title__text').text.strip()
        TITLE.append(title)

    content_divs = soup.find_all('div', class_="sc-b189961a-7 feoqjK cli-title-metadata")
    for div in content_divs:
        year = div.find('span', class_='sc-b189961a-8 kLaxqf cli-title-metadata-item').text.strip()
        YEAR.append(year)

    content_divs = soup.find_all('div', class_="sc-e2dbc1a3-0 ajrIH sc-b189961a-2 fkPBP cli-ratings-container")
    for div in content_divs:
        rating = div.text[0:3].strip()
        RATING.append(rating)

    content_divs = soup.find_all('div', class_="ipc-poster ipc-poster--base ipc-poster--dynamic-width ipc-sub-grid-item ipc-sub-grid-item--span-2")
    for div in content_divs:
        src = div.find('img', class_='ipc-image')
        icon = src.attrs.get('src')
        ICON.append(icon)

else:
    print(f'Failed to fetch the page. Status code: {response.status_code}')


movie_data = []

for i in range(len(TITLE)):
    movie = {
        "TITLE": TITLE[i].split('. ')[1],
        "YEAR": int(YEAR[i]),
        "RATING": RATING[i],
        "ICON": ICON[i]
    }
    movie_data.append(movie)


with open('main.json', 'w') as json_file:
    json.dump(movie_data, json_file, indent=4)