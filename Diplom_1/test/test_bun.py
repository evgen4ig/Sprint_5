from praktikum.bun import Bun
from data import Data


class TestBun:
    # Проверяем что метод возвращает верное название булки
    def test_get_name_return_true_name(self):
        bun = Bun(Data.buns[0].get("name"), Data.buns[0].get("price"))
        name = bun.get_name()

        assert name == Data.buns[0].get("name")

    # Проверяем что метод вернул верную цену булки
    def test_get_price_return_true_price(self):
        bun = Bun(Data.buns[1].get("name"), Data.buns[1].get("price"))
        price = bun.get_price()

        assert price == Data.buns[1].get("price")