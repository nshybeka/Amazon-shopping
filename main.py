import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com/dp/B01N8RAZB1/ref=sbl_dpx_kitchen-electric-cookware_B0B7P646FD_0?th=1"
header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
    "Accept-Language": "en-US,en;q=0.5"
}

my_price = 100
response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, 'lxml')

price_div = soup.find("div", class_="a-section a-spacing-none aok-align-center")
price_one = price_div.find("span", class_="a-price-whole")
price_two = price_div.find("span", class_="a-price-fraction")
price = f"{price_one.text}{price_two.text}"
print(f"Price now is {price} $")

if float(price) < my_price:
    print("The price really good!")
else:
    print("The price is high.")




