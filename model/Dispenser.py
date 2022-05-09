from model.Card import Card
from model.Drink import Drink
from model.Column import Column
from model.CodeNotFound import CodeNotFound


class Dispenser:
    def __init__(self):
        self.drinks = list()
        self.cards = list()
        self.columns = {
            1: Column("", 0),
            2: Column("", 0),
            3: Column("", 0),
            4: Column("", 0)
        }

    def add_drink(self, code, name, price):
        drink = Drink(code, name, price)
        self.drinks.append(drink)

    def get_price(self, code):
        for drink in self.drinks:
            if drink.code == code:
                return drink.price
        raise CodeNotFound()

    def get_name(self, code):
        for drink in self.drinks:
            if drink.code == code:
                return drink.name
        raise CodeNotFound()

    def add_card(self, code):
        card = Card(code)
        self.cards.append(card)

    def get_card(self, code):
        for card in self.cards:
            if card.code == code:
                return card
        raise CodeNotFound()

    def charge_card(self, code, credit):
        for card in self.cards:
            if card.code == code:
                card.credit += credit

    def get_credit(self, code):
        for card in self.cards:
            if card.code == code:
                return card.credit
        raise CodeNotFound()

    def update_column(self, num_column, drink_name, num_can):
        self.columns[num_column] = Column(drink_name, num_can)

    def get_column(self, drink_name):
        for index, column in self.columns.items():
            if column.name_drink == drink_name:
                return index, column

    def get_num_can(self, drink_name):
        num = 0
        for column in self.columns.values():
            if column.name_drink == drink_name:
                num += column.num_can
        return num

    def deliver_drink(self, drink_code, card_code):
        credit = self.get_credit(card_code)
        price = self.get_price(drink_code)
        drink_name = self.get_name(drink_code)
        num_can = self.get_num_can(drink_name)
        card = self.get_card(card_code)
        num_column, column = self.get_column(drink_name)
        if credit < price:
            raise Exception("Credit insufficient")
        if num_can < 1:
            raise Exception("Out of drink")
        card.credit -= price
        column.num_can -= 1
        return num_column
