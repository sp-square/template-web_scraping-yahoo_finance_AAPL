import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://finance.yahoo.com/quote/AAPL?p=AAPL"

response = requests.get(url)
response_text = response.text

soup = BeautifulSoup(response_text, features='html.parser')

tables = soup.find_all("table")
# print(len(tables))
# print(tables)
print()
my_table_cells = tables[0].find_all('td') + tables[1].find_all('td')

names = []
values = []

for idx in range(len(my_table_cells)):
    if idx % 2 == 0:
        names.append(my_table_cells[idx].text)
    else:
        values.append(my_table_cells[idx].text)

print(names)
print(values)

df = pd.DataFrame({
    'names': names,
    'values': values
})
print(df)
