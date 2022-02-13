from mw import Data


class Post(Data):
    objects = []
    def __init__(self, title, text, date, author):
        self.title = title
        self.text = text
        self.date = date
        self.author = author
Post.load()


class Product(Data):
    objects = []
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
Product.load()


class User(Data):
    objects = []
    def __init__(self, username, password):
        self.username = username
        self.password = password
User.load()
