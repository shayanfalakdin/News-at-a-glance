from flask import Blueprint , render_template

from currency.models.currency import get_currency

currency_blueprint = Blueprint('currency_blueprint', __name__ , template_folder='templates')

@currency_blueprint.route('/currency')
def currency():
    return render_template("currency_news.html" , currency_data = get_currency())   