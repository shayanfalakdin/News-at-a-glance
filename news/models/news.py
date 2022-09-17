from flask import render_template
from requests import request

def get_news_data():
    url = "https://newsapi.org/v2/top-headlines?country=us&category=sports&pageSize=20&apiKey=4446789348d24622a3881063f7d144d7"
    response = request("GET", url).json()
    news = response["articles"]
    return news

def get_ten_news():
    url = "https://newsapi.org/v2/top-headlines?country=us&pageSize=8&category=sports&apiKey=4446789348d24622a3881063f7d144d7"
    response = request("GET", url).json()
    news = response["articles"]
    return news
