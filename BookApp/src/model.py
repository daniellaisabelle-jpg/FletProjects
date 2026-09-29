class Book(object):
    def __init__(self, title:str, author: str, desc:str, price:float):
        self.title = title
        self.author = author
        self.desc = desc
        self.price = price
    def __str__(self) -> str:
        return f'Book({self.title}, {self.author})'