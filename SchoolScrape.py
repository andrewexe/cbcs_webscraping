import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://www.browardschools.com/cypressbay")

soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all(class_='ui-article')

for article in articles:
    title = article.find('a').get_text()
    print(title)