from flask import render_template, request, Blueprint, redirect, url_for
from app.main1 import *

bp = Blueprint("add_word", __name__, template_folder="../templates")


@bp.route("/addword", methods=["GET", "POST"])
def AddWord():
    print("gelen istek tipi****", request.method)

    if request.method == "POST":

        word = request.form.get("word")
        meaning = request.form.get("meaning")
        sample = request.form.get("sample")
        if word and meaning and sample:
            word_list = Dictionary("app/deneme.json")
            word_list.insert_word(word=word, meaning=meaning, sample=sample)

            return redirect(url_for("show_list.ShowList"))

    return render_template('add_word.html')
