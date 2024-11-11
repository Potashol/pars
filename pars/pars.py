from LxmlSoup import LxmlSoup
import requests


html = requests.get('https://quotes.toscrape.com/').text

soup = LxmlSoup(html)

with open('html.txt', "w", encoding="utf-8") as f:
    f.write(html)

links = soup.find_all('span', class_='text')

file = open ('cntent.json', "w", encoding="utf-8")
for i, link in enumerate(links):
    url = link.get("href") 
    name = link.text()
    autor = soup.find_all('small', class_='author')[i].text()
    file.write(str(i) + '\n')
    file.write(f"Name - {name}" + '\n')
    file.write(f"Autor - {autor}" + '\n')

file.close()
    


