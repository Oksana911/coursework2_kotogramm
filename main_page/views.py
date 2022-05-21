import logging

from flask import Blueprint, render_template, request

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


@main_blueprint.route("/search")
def search_by_substring_page():
    """Страница поиска постов по слову"""
    # logging.info("Открытие страницы поиска по слову")
    s = request.args.get("s", "")
    posts = utils.search_for_posts(s, POST_PATH)
    posts_count = len(posts)
    return render_template("search.html", posts=posts, s=s, posts_count=posts_count)

@main_blueprint.route("/search/<username>", methods=["GET", "POST"])
def search_by_username_page(username):
    """Страница поиска постов по юзеру"""
    # logging.info("Открытие страницы поиска постов по юзеру")
    user_name = request.args.get("item__username")
    posts = utils.get_posts_by_user(user_name, POST_PATH)
    return render_template("user-feed.html", posts=posts, user_name=user_name)

