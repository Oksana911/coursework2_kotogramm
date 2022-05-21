import logging

from flask import Blueprint, render_template, request, jsonify

import utils

from config import *

api_blueprint = Blueprint("api_blueprint", __name__, template_folder="templates")


@api_blueprint.route("/api/main_page")
def api_main_page():
    """Главная страница показывает все посты"""
    # all_posts = utils.get_all(POST_PATH)
    return jsonify({"content": "Страница ленты"})


@api_blueprint.route("/api/post/<int:post_id>")
def api_one_post_page(post_id):
    """Страница одного поста по его номеру"""
    # post = utils.get_post_by_pk(post_id, POST_PATH)
    return jsonify({"content": "Страница одного поста"})


