import logging

from flask import Blueprint, render_template, request

import utils

from config import *

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")
# logging.basicConfig(filename="logger.log", level=logging.INFO)


@main_blueprint.route("/")
def main_page():
    """Главная страница показывает все посты"""
    # logging.info("Открытие главной страницы")
    all_posts = utils.get_all(POST_PATH)
    return render_template("index.html", all_posts=all_posts)


@main_blueprint.route("/post/<int:post_id>")
def search_by_post_id_page(post_id):
    """Страница одного поста по его номеру"""
    # logging.info("Открытие страницы поста по его номеру")
    post = utils.get_post_by_pk(post_id, POST_PATH)
    post_id = post["pk"]
    comments = utils.get_comments_by_post_id(post_id, COMMENTS_PATH)
    comments_count = len(comments)


    return render_template("post.html", post=post, comments=comments, comments_count=comments_count)


# @main_blueprint.route("/search/<s>", methods=["POST"])
# def search_by_substring_page(s):
#     """Страница поиска постов по слову"""
#     s = request.args.get("s", "")
#     # logging.info("Открытие страницы поиска")
#     # posts = utils.get_all("data/data.json")
#     result = utils.search_for_posts(s, "data/data.json")
#
#     return render_template("post.html", posts=result, s=s)
#
# @main_blueprint.route("/search/<username>")
# def search_by_username_page():
#     """Страница поиска постов по юзеру"""
#     # s = request.args.get("s", "")
#     # # logging.info("Открытие страницы поиска")
#     # # posts = utils.get_all("data/data.json")
#     # result = utils.search_for_posts(s, "data/data.json")
#     #
#     # return render_template("post.html", posts=result, s=s)