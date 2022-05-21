from flask import Blueprint, jsonify

api_blueprint = Blueprint("api_blueprint", __name__, template_folder="templates")


@api_blueprint.route("/api/main_page")
def api_main_page():
    """Главная страница показывает все посты"""
    return jsonify({"content": "Страница ленты"})


@api_blueprint.route("/api/post/<int:post_id>")
def api_one_post_page(post_id):
    """Страница одного поста по его номеру"""
    return jsonify({"content": "Страница одного поста"})


