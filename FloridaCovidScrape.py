import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://www.worldometers.info/coronavirus/country/us")

soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find(id = 'usa_table_countries_today')
rows = table.find_all('tr')
for row in rows:
    td = row.find('td')
    if(td != None):
        state = td.get_text()
        #print(state)
        state = state.strip()
        if state == 'Florida':
            #print(row)
            column_tds = row.find_all('td')
            print("State: " + str(column_tds[0].get_text().strip()))
            print("Total Cases: " + str(column_tds[1].get_text().strip()))
            print("New Cases: " + str(column_tds[2].get_text().strip()))
            print("Total Deaths: " + str(column_tds[3].get_text().strip()))
            print("New Deaths: " + str(column_tds[4].get_text().strip()))