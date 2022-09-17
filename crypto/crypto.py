from flask import Blueprint, make_response, redirect, render_template, url_for
from requests import request
from crypto.models.crypto import get_crypto
import sys

crypto_blueprint = Blueprint('crypto_blueprint', __name__ , template_folder='templates')

@crypto_blueprint.route("/crypto/")
def crypto():
    return render_template("crypto_news.html", crypto_data=get_crypto())