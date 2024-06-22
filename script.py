from bs4 import BeautifulSoup
import requests
import json

res= requests.get('http://books.toscrape.com/')
print(res)
with open('data.html',"w") as f:
  f.write(res.text)
soup= BeautifulSoup(res.text)

titles=soup.find_all('h3')
print(len(titles))
for t in titles:
    print(t.get_text())
if len(titles) >= 3:
        third_title = titles[2].get_text()
        print("The 3rd book title is:", third_title)
else:
        print("There are fewer than 3 book titles on the page.")
data=[]
for t in titles:
        data.append(t.get_text())

with open('data.json', 'w') as f:
      json.dump(data,f, indent=2)


