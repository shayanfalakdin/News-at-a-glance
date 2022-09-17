from flask import Blueprint, make_response, redirect, render_template, url_for
from requests import request
from news.models.news import get_news_data

news_blueprint = Blueprint('news_blueprint', __name__ , template_folder='templates')

@news_blueprint.route("/news/")
def get_news():
    return render_template('sport_news.html', news_arry=get_news_data())