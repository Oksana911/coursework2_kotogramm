import json
from json import JSONDecodeError


def get_all(path):
    """возвращает все посты/комментарии"""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print("Файл не найден")
    except JSONDecodeError:
        print("Файл не удается преобразовать")


def get_posts_by_user(user_name, path):
    """возвращает посты определенного пользователя"""
    if type(user_name) != str:
        raise TypeError

    data = get_all(path)
    posts_by_user = []

    for post in data:
        if post["poster_name"].lower() == user_name.lower():
            posts_by_user.append(post)
    return posts_by_user


def get_comments_by_post_id(post_id, path):
    """возвращает комментарии определенного поста"""
    if type(post_id) != int:
        raise TypeError

    data = get_all(path)
    comments = []

    for comment in data:
        if comment["post_id"] == post_id:
            comments.append(comment)
    return comments


def search_for_posts(query, path):
    """возвращает список постов по ключевому слову"""
    if type(query) != str:
        raise TypeError

    data = get_all(path)
    posts_by_query = []

    for post in data:
        if query.lower() in post["content"].lower():
            posts_by_query.append(post)
    return posts_by_query


def get_post_by_pk(pk, path):
    """возвращает один пост по его номеру"""
    if type(pk) != int:
        raise TypeError

    data = get_all(path)

    for post in data:
        if post["pk"] == pk:
            return post
