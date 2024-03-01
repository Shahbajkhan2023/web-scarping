import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone'
r = requests.get(url)
# print(r)

soup = BeautifulSoup(r.text, "html.parser")
# print(soup)


# boxes = soup.find_all('div', class_="col-md-4 col-xl-4 col-lg-4")
# # print(boxes)
# # we can get the lenght of boxes using the lenght function of python
# print(len(boxes))


names = soup.find_all('a', class_="title")
# print(names)

# for i in names:
#     print(i.text)

prices = soup.find_all('h4', class_="float-end price card-title pull-right")
# print(prices)

for i in prices:
    print(i.text)