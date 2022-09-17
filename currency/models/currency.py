import requests

def get_currency():
    url = 'https://api.exchangerate.host/latest'
    response = requests.get(url).json()
    data = response["rates"]
    return data
    
def get_five_currency():
    url = 'https://api.exchangerate.host/latest?symbols=USD,EUR,IRR'
    response = requests.get(url).json()
    data = response["rates"]
    return data