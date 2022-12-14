import sqlite3

conn = sqlite3.connect('shop_project.db')
cursor = conn.cursor()

shop = '''CREATE TABLE IF NOT EXISTS shop(code INTEGER, title TEXT, price DOUBLE ,weight DOUBLE, brend STRING, des TEXT, img STRING) '''
cursor.execute(shop)

