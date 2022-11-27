from flask import render_template, request, Blueprint
from app.main1 import *

bp = Blueprint("search", __name__, template_folder="../templates")


@bp.route("/searchlist", methods=["GET", "POST"])
def SearchList():
    if request.method == 'POST':
        value = request.form.get("value")

        if value:
            meaning_list = Dictionary("app/deneme.json").search_word(value=value)
            data = meaning_list
            print(meaning_list)
            data_value= value
            return render_template('search_result.html', context=data,word_value=data_value)

    return render_template('search.html')
