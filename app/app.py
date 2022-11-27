from flask import Flask
from .views import home,add_word,delete_word,search,show_list,update_word

def create_app():

    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config.from_pyfile("config.py")

    if app.config["VERSION"] =="1.0.1":
        pass
    elif app.config["VERSION"] == "1.0.2":
        pass

    app.register_blueprint(home.bp)
    app.register_blueprint(add_word.bp)
    app.register_blueprint(delete_word.bp)
    app.register_blueprint(search.bp)
    app.register_blueprint(show_list.bp)
    app.register_blueprint(update_word.bp)



    return app