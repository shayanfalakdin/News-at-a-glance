from flask import Flask

from crypto.crypto import crypto_blueprint
from news.news import news_blueprint
from currency.currency import currency_blueprint
from home.home import home_blueprint

app = Flask(__name__)

app.register_blueprint(news_blueprint)
app.register_blueprint(crypto_blueprint)
app.register_blueprint(currency_blueprint)
app.register_blueprint(home_blueprint)


if __name__ == '__main__':
    app.run(debug=True)
