import pandas as pd
import requests
from bs4 import BeautifulSoup
product_name = []
prices = []
Description = []
Reviews = []


for i in range(1, 10):
        url = "https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)

        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        box = soup.find('div', class_="_1YokD2 _3Mn1Gg")

        names = box.find_all("div", class_="_4rR01T")
        for i in names:
                name = i.text
                product_name.append(name)
        # print(len(product_name))




        price = box.find_all('div', class_="_30jeq3 _1_WHN1")
        for i in price:
                name = i.text
                prices.append(name)
        # print(len(prices))



        desc = box.find_all('ul', class_='_1xgFaf')
        for i in desc:
                name = i.text
                Description.append(name)
        # print(len(Description))




df = pd.DataFrame({'Product Name': product_name, "Prices": prices, 'Description': Description, "REviews": Reviews})
df.to_csv('bbbc')








    # np = soup.find('a', class_="_1LKTO3").get("href")
    # cnp = "https://www.flipkart.com"+np
    # print(cnp)

# url = cnp
# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'html.parser')
