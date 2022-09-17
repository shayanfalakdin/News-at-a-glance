from flask import Blueprint, make_response, render_template
from requests import request

from news.models.news import get_ten_news
from currency.models.currency import get_five_currency
from crypto.models.crypto import get_five_crypto

home_blueprint= Blueprint('home_news', __name__ , template_folder='templates')

@home_blueprint.route("/")

def get_news():
    return render_template('home_page.html', news_arry=get_ten_news() , currency_data = get_five_currency() , crypto_data=get_five_crypto())

