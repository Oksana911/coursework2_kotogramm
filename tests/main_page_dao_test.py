import pytest

from main_page.dao.main_page_dao import MainPageDao

class TestMainPageDao:

    @pytest.fixture()
    def main_page_dao(self):
        return MainPageDao("data/data.json")

# тестируем получение всех постов
    def test_get_all_check_type(self, main_page_dao):
        posts = main_page_dao.get_all()
        assert type(posts) == list, "Список постов должен быть list"
        assert type(posts[0]) == dict, "Один пост должен быть dict"

    def test_get_all_has_keys(self, main_page_dao):
        posts = main_page_dao.get_all()
        keys_expected = ["poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"]
        for post in posts:
            keys = post.keys()
            assert set(keys) == keys_expected, "Потерялся ключ"


# тестируем получение одного поста
    def test_get_one_check_type(self, main_page_dao):
        post = main_page_dao.get_post_by_pk()
        assert type(post) == dict, "Один пост должен быть dict"
