import requests
from bs4 import BeautifulSoup


def boothscrape(url):
    soup = getsoup(url)
    itemcards = soup.find_all('li', class_='item-card')

    itemdatas = []
    itemcard = itemcards[0]
    itemid = itemcard.get('data-product-id')
    itemthumbnailimageurl = itemcard.find('a', class_='item-card__thumbnail-image').get('data-original')
    itemcategory = itemcard.find('div', class_='item-card__category').text
    itemtitle = itemcard.find('div', class_='item-card__title').text
    shopurl = itemcard.find('a', class_='item-card__shop-name-anchor').get('href')
    shopthumbnailurl = itemcard.find('img', class_='user-avatar').get('src')
    shopname = itemcard.find('div', class_='item-card__shop-name').text
    itemdata = [itemid, itemthumbnailimageurl, itemcategory, itemtitle, shopurl, shopthumbnailurl, shopname]
    itemdatas.append(itemdata)

    return itemdatas


def getsoup(url):
    reps = requests.get(url)
    html = reps.content
    soup = BeautifulSoup(html, 'lxml')
    return soup
