from flask import render_template, request, Blueprint, redirect, url_for
from app.main1 import *

bp = Blueprint("update_word", __name__, template_folder="../templates")


@bp.route("/updateword", methods=["GET", "POST"])
def UpdateWord():

    if request.method == 'POST':
        new_value = request.form.get("new_value")

        if new_value:
            word_list = Dictionary("app/deneme.json")
            word = request.form.get("word")
            meaning = request.form.get("meaning")
            new_value = request.form.get("new_value")
            word_list.edit_word(word=word, meaning=meaning, new_value=new_value)

            return redirect(url_for("show_list.ShowList"))

    return render_template('update.html')
