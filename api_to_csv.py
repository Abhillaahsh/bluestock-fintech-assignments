import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "ids": "bitcoin,ethereum,solana"
}

response = requests.get(url, params=params)

print("Status Code:", response.status_code)

data = response.json()

df = pd.DataFrame(data)

df = df[
    [
        "id",
        "symbol",
        "name",
        "current_price",
        "market_cap",
        "total_volume",
        "price_change_percentage_24h"
    ]
]

df.to_csv("crypto_market_data.csv", index=False)

print(df)
print("CSV created successfully!")