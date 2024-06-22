import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv
res=requests.get('http://books.toscrape.com/')
print(res)
with open('data.html',"w") as f:
  f.write(res.text)
soup= BeautifulSoup(res.text)
books = []
for book in soup.find_all('article', class_='product_pod'):
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    availability = book.find('p', class_='instock availability').text.strip()
    books.append([title, price, availability])
df = pd.DataFrame(books, columns=['Title', 'Price', 'Availability'])
df.to_csv('books.csv', index=False)
print('Data has been saved to books.csv')

