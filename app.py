import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/quote/AAPL?p=AAPL"

response = requests.get(url)
response_text = response.text

soup = BeautifulSoup(response_text, features='html.parser')

tr_tags = soup.find_all("tr")
# print(tr_tags)
# print(tr_tags[0])
# print(tr_tags[0].text)
# print(tr_tags[0].td)
# print(tr_tags[0].td.text)
# print(tr_tags[0].td.span)
# print(tr_tags[0].td.span.text)
# print(tr_tags[0].span.text)
# print(tr_tags[0].contents)
print(tr_tags[0].contents[0].text)
print(tr_tags[0].contents[1].text)

# find all the td tags that have this class name
# td_tags = soup.find_all('td', class_="C($primaryColor) W(51%)")
# print(td_tags)

# find the td tag that has this specific attribute
print(tr_tags[0].find('td', attrs={"data-test": "PREV_CLOSE-value"}))
print(tr_tags[0].find('td', attrs={"data-test": "PREV_CLOSE-value"}).text)
