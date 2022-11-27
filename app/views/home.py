from flask import render_template, request, Blueprint,redirect,url_for

bp = Blueprint("home",__name__,template_folder="../templates")

@bp.route("/")

def Index():
    return render_template("index.html")