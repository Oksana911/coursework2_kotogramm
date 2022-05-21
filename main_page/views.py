import logging

from json import JSONDecodeError

from flask import Blueprint, render_template, request

from config import *

from .dao.main_page_dao import MainPageDao
from .dao.comments_dao import CommentsDao

main_page_dao = MainPageDao(POST_PATH)
comments_dao = CommentsDao(COMMENTS_PATH)

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")


# logging.basicConfig(filename="logger.log", level=logging.INFO)


@main_blueprint.route("/")
def main_page():
    """Главная страница показывает все посты"""
    # logging.info("Открытие главной страницы")
    try:
        all_posts = main_page_dao.get_all()
        return render_template("index.html", all_posts=all_posts)
    except FileNotFoundError:
        print("Файл не найден")
    except JSONDecodeError:
        print("Файл не удается преобразовать")


@main_blueprint.route("/post/<int:post_id>")
def search_by_post_id_page(post_id):
    """Страница одного поста по его номеру"""
    # logging.info("Открытие страницы поста по его номеру")
    try:
        post = main_page_dao.get_post_by_pk(post_id)
        post_id = post["pk"]
        comments = comments_dao.get_comments_by_post_id(post_id)
        comments_count = len(comments)
        return render_template("post.html", post=post, comments=comments, comments_count=comments_count)
    except:
        return "Ошибка при загрузке поста/комментариев"



@main_blueprint.route("/search")
def search_by_substring_page():
    """Страница поиска постов по слову"""
    # logging.info("Открытие страницы поиска по слову")
    s = request.args.get("s", "")
    posts = main_page_dao.search_for_posts(s)
    posts_count = len(posts)
    return render_template("search.html", posts=posts, s=s, posts_count=posts_count)


@main_blueprint.route("/search/<username>")
def search_by_username_page(username):
    """Страница поиска постов по юзеру"""
    # logging.info("Открытие страницы поиска постов по юзеру")
    user_name = request.args.get("item__username")
    posts = main_page_dao.get_posts_by_user(username)
    return render_template("user-feed.html", posts=posts, user_name=user_name)
