import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

URL_TEMPLATE = "https://steamcommunity.com/market/"
FILE_NAME = "test.csv"


def parse(url = URL_TEMPLATE):
    result_list = {'href': [], 'title': [], 'about': []}
    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    case_names = soup.find_all('h2', class_='market_listing_item_name_block')
    case_info = soup.find_all('p', class_='normal_price')
    for name in case_names:
        result_list['href'].append('https://steamcommunity.com'+name.a['href'])
        result_list['title'].append(name.a['title'])
    for info in case_info:
        result_list['about'].append(info.text)
    return result_list


df = pd.DataFrame(data=parse())
df.to_csv(FILE_NAME)