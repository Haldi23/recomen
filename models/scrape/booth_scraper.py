import requests
from bs4 import BeautifulSoup


def scrape_booth(url):
    soup = get_soup(url)
    item_cards = soup.find_all('li', class_='item-card')

    item_datas = []
    # for item_card in item_cards:  時が来たら
    item_card = item_cards[0]
    item_id = item_card.get('data-product-id')
    item_thumbnail_src = item_card.find('a', class_='item-card__thumbnail-image').get('data-original')
    item_category = item_card.find('div', class_='item-card__category').text
    item_title = item_card.find('div', class_='item-card__title').text
    shop_url = item_card.find('a', class_='item-card__shop-name-anchor').get('href')
    shop_thumbnail_src = item_card.find('img', class_='user-avatar').get('src')
    shop_name = item_card.find('div', class_='item-card__shop-name').text
    item_data = [item_id, item_thumbnail_src, item_category, item_title, shop_url, shop_thumbnail_src, shop_name]
    item_datas.append(item_data)

    return item_datas


def get_soup(url):
    reps = requests.get(url)
    html = reps.content
    soup = BeautifulSoup(html, 'lxml')
    return soup
