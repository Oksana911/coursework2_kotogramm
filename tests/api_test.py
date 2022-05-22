# from tests.conftest import test_client
import pytest

from app import app

class TestApiMainPage:

    # @pytest.fixture
    # def test_client(self):
    #     test = app.run()
    #     return test.test_client()

    @pytest.fixture()
    def keys(self):
        return {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

    def test_api_main_page(self, keys):
        """ Проверяем, возвращает ли страница всех постов нужный статус-код и нужный формат данных """
        response = app.test_client().get('/api/main_page', follow_redirects=True)
        assert response.status_code == 200, "Статус код неверный"
        assert response.mimetype == "application/json", "Получен не JSON"
        assert type(response.data) == list, "Данные должны быть списком"
        assert keys in response.data, "В данных JSON отсуствуют нужные ключи"

    def test_api_post_page(self, keys):
        """ Проверяем, возвращает ли страница одного поста нужный статус-код и нужный формат данных """
        response = app.test_client().get('/api/post/1', follow_redirects=True)
        assert response.status_code == 200, "Статус код неверный"
        assert response.mimetype == "application/json", "Получен не JSON"
        assert type(response.data) == dict, "Данные должны быть словарем"
        assert keys in response.data, "В данных JSON отсуствуют нужные ключи"
