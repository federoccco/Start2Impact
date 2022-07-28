import requests  # In order to make an http request, i import the requests module
import os  # I'll need this to call a variable
import json  # To save info in a JSON file
from datetime import datetime  # I'll need it to rename the .json file i'll create


# Requests module syntax require requests.get, inside the parenthesis we have to provide some **kwargs
# Specifically url, params, header

# URL: saving the endpoint in a constant in order to not repeat the string when making requests
# Constant usually are declared in caps lock


COINMARKETCAP_ENDPOINT = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

# Headers: A dictionary necessary to authenticate when making the request
CMC_API_KEY = os.environ["CMC_API_KEY"]  # Api key is a private data, i created an environment variable
headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": CMC_API_KEY
}

# Params is a dictionary that contains the parameters that will help us filtering information i am interested in:
step1_parameters = {
    "start": 1,
    "limit": 1,  # We care about the first one, thus we stop right after that
    "convert": "USD",
    "sort": "volume_24h"  # Sort allows us to sort based on the volume in the last 24 hours
}


# 1 - Most volume ($) crypto in the last 24 hours

# Making the request, with .json() at the end i can make the r variable a json
r_1 = requests.get(url=COINMARKETCAP_ENDPOINT, params=step1_parameters, headers=headers).json()
last_24h_most_volume = r_1["data"][0]["symbol"]


# 2.1 - Top 10 crypto (percentage increase in the last 24 hours)

step2_best_parameters = {
    "start": 1,
    "limit": 10,
    "convert": "USD",
    "sort": "percent_change_24h"  # Ordering by the percentage variation in the last 24 hours
}
r2_1 = requests.get(url=COINMARKETCAP_ENDPOINT, params=step2_best_parameters, headers=headers).json()
top10_24h_percentage = [currency["symbol"] for currency in r2_1["data"]]


# 2.2 - Flop 10 crypto (percentage increase in the last 24 hours)

step2_worst_parameters = {
    "start": 1,
    "limit": 10,
    "convert": "USD",
    "sort": "percent_change_24h",
    "sort_dir": "asc"  # Starting from the bottom
}
r2_1 = requests.get(url=COINMARKETCAP_ENDPOINT, params=step2_worst_parameters, headers=headers).json()
flop10_24h_percentage = [currency["symbol"] for currency in r2_1["data"]]


# 3 - The amount of money necessary to buy a single unit of each in the top 20 crypto* leaderboard

step3_parameters = {
    "start": 1,
    "limit": 20,
    "convert": "USD"
}
r3 = requests.get(url=COINMARKETCAP_ENDPOINT, params=step3_parameters, headers=headers).json()
prices = [price["quote"]["USD"]["price"] for price in r3["data"]]
total_prices = sum(prices)


# 4 - The amount of money necessary to buy a single unit of all those crypto whose volume is above 76'000'000$
# In the last 24 hours

step4_parameters = {
    "start": 1,
    "limit": 5000,
    "convert": "USD",
    "volume_24h_min": 76_000_000
}
r4 = requests.get(url=COINMARKETCAP_ENDPOINT, params=step3_parameters, headers=headers).json()
volume_prices = [price["quote"]["USD"]["price"] for price in r4["data"]]
total_volume_prices = sum(volume_prices)


# 5 - The percentage loss (earnings) if you would have bought a single unit of each in the top 20 crypto* leaderboard
# The day before running the script (assuming the leaderboard has not changed)

# In this step i need to get some data utilizing the same response i got in the step 3:
# Percentage variation in the last 24 hours
percentage = [percentage["quote"]["USD"]["percent_change_24h"] for percentage in r3["data"]]

# The price of crypto currency 24 hours before, i.e. by the time of acquisition:
initial_prices = [prices[n] / (percentage[n] + 1) for n in range(len(prices))]
total_initial_prices = sum(initial_prices)

# I can get the total percentage variation by dividing the difference between the sum of final and starting prices
# By the sum of starting prices

total_variation_percentage = (total_prices - total_initial_prices) / total_initial_prices

# Making a dictionary with the infos i want to save in the file:
data = {
    "last_24h_most_volume": last_24h_most_volume,
    "top10_24h_percentage": top10_24h_percentage,
    "flop10_24h_percentage": flop10_24h_percentage,
    "money_to_buy_a_unit_top20": total_prices,
    "money_to_buy_a_unit_volume_over_76kk": total_volume_prices,
    "percentage_profit_buying_unit_top20": total_variation_percentage
}
today = datetime.now().strftime("%d-%m-%Y")  # Setting the date format to dd-mm-yyyy
with open(f"{today}.json", "w") as data_file:  # With allow us to not worry about closing the file
    json.dump(data, data_file, indent=4)  # Indent in order to better format and make it more readable


