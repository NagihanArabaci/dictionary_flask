from flask import render_template, request, Blueprint, redirect, url_for
from app.main1 import *

bp = Blueprint("delete_word", __name__, template_folder="../templates")


@bp.route("/deleteword", methods=["GET", "POST"])
def DeleteWord():

    if request.method == 'POST':
        value = request.form.get("value")
        if value:
            word_list = Dictionary("app/deneme.json")
            word_list.delete_word(value=value)
            return redirect(url_for("show_list.ShowList"))
    return render_template('delete.html')
