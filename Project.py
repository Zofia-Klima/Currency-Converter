# Currency calculator

print("Currency Calculator to PLN")
currency = input("Enter currency (e.g., USD, EUR): ").upper()
print(f"Selected currency: {currency}")

#https://api.nbp.pl/api/exchangerates/tables/A/?format=json

import requests

url = f"https://api.nbp.pl/api/exchangerates/rates/A/{currency}/2024-06-24?format=json"

response = requests.get(url)
data = response.json()

exchange_rate = data["rates"][0]["mid"]
print(f"1{currency} = {exchange_rate}PLN ON 24-06-24")