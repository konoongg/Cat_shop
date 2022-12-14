import requests
from bs4 import BeautifulSoup
import sqlite3

URL = "https://yokot.ru/koshki/lechebnyy-korm/royal-canin-royal-kanin/purina-purina/hills-hils/page"
HEADERS = {'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}
HOST = 'https://yokot.ru/'
conn = sqlite3.connect('shop_project.db')
cursor = conn.cursor()
tovar_link = []
cods_tup = []

cods = ''' SELECT code FROM shop '''
cods = cursor.execute(cods).fetchall()
for i in cods:
    cods_tup.append(int(i[0]))     
print(cods_tup)


for i in range(1,12):
    r = requests.get(URL+str(i),headers=HEADERS)
    soup = BeautifulSoup(r.text,'html.parser')
    tovars = soup.findAll('a',class_='item_page_link')
    for i in tovars:
        tovar_link.append(i['href'])
for i in tovar_link:
    r = requests.get(i,headers=HEADERS)
    soup = BeautifulSoup(r.text,'html.parser')
    code = int(soup.find('div',class_='item_code').get_text(strip=True)[4:])
    if code in cods_tup:
        print(code, " skip" )
        continue
    title = soup.find('div',class_='item_title').get_text(strip=True)
    price = soup.find('span', class_= 'item_price_current').get_text(strip=True)[5:-1]
    weight = soup.find('div',class_='item_weight').get_text(strip=True)[4:-2]
    brend = soup.find('span',class_='item_country').get_text(strip=True)[6:]
    des = soup.find('div',class_='item_description').get_text(strip=True). replace('Ёжкин кот','')
    img = soup.find('img',class_='item_big_image')['src']

    conn = sqlite3.connect('shop_project.db')
    cursor = conn.cursor()
    shop_bd = '''INSERT INTO shop (code, title, price, weight, brend, des, img ) VALUES(?,?,?,?,?,?,?)'''
    cursor.execute(shop_bd, [code, title, price, weight,brend, des, img])   
    conn.commit()
    print(code)
