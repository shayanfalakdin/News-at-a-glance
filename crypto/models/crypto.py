from requests import request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
def get_crypto():

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {'start': '1', 'limit': '5000', 'convert': 'USD'}
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '9b1e29af-632d-4a40-b772-02702a5d2963  ',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters).json()
        crypto_data = response["data"]
        return crypto_data
    except (ConnectionError, Timeout, TooManyRedirects) as error:
        return error

def get_five_crypto():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {'start': '1', 'limit': 5, 'convert': 'USD'}
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '9b1e29af-632d-4a40-b772-02702a5d2963  ',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters).json()
        crypto_data = response["data"]
        return crypto_data
    except (ConnectionError, Timeout, TooManyRedirects) as error:
        return error