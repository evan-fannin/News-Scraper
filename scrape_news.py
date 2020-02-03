import requests

from datetime import datetime

from bs4 import BeautifulSoup

import pandas as pd

import os.path

r = requests.get('https://www.reuters.com/news/us')

news = r.text

time_gathered = datetime.ctime(datetime.now())

soup = BeautifulSoup(news, 'html.parser')

brief = soup.find_all("p", class_="FeedItemLede_lede")

category = soup.find_all("a", class_="FeedItemMeta_channel")

time_written = soup.find_all("span", class_="FeedItemMeta_date-updated")

headline = soup.body.find_all("h2", class_="FeedItemHeadline_headline FeedItemHeadline_full")

for i, entry in enumerate(brief):
    brief[i] = entry.string.replace(u'\xa0', u' ')

for i, entry in enumerate(category):
    category[i] = entry.string.replace(u'\xa0', u' ')

for i, entry in enumerate(time_written):
    time_written[i] = entry.string.replace(u'\xa0', u' ')

for i, entry in enumerate(headline):
    headline[i] = entry.string.replace(u'\xa0', u' ')

dict = {'category': category, 'time_written': time_written, 'time_gathered': time_gathered, 'headline': headline, 'brief': brief}

df = pd.DataFrame(dict)

if os.path.isfile('downloads/us_news.csv'):
    with open('downloads/us_news.csv', 'a') as file:
        df.to_csv(file, header=False, index=False)
else:
    df.to_csv('~/downloads/us_news.csv', header=False, index=False)