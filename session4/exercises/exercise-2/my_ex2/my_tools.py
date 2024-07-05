import requests

def fetch_currency_conversion(data):
    # Unpack the tuple into amount, from_currency, and to_currency
    amount, from_currency, to_currency = data
    url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data['rates'][to_currency]
        print(f"{amount} {from_currency} = {rate} {to_currency}")
        return(f"{amount} {from_currency} = {rate} {to_currency}")
    else:
        return("Failed to fetch data from API")
