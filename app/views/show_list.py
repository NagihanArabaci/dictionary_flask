from flask import render_template, request, Blueprint
from app.main1 import *

bp = Blueprint("show_list", __name__, template_folder="../templates")


@bp.route("/showlist", methods=["GET"])
def ShowList():
    word_list = Dictionary("app/deneme.json").word_list
    data=word_list

    return render_template('list_words.html', context=data)
