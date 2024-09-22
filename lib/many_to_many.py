# many_to_many.py
class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author class")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book class")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)
        author.add_contract(self)
        book.add_contract(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]

class Author:
    def __init__(self, name):
        self.name = name
        self._contracts = []

    def add_contract(self, contract):
        self._contracts.append(contract)

    def contracts(self):
        return self._contracts

    def books(self):
        return list(set(contract.book for contract in self._contracts))

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)

class Book:
    def __init__(self, title):
        self.title = title
        self._contracts = []

    def add_contract(self, contract):
        self._contracts.append(contract)

    def contracts(self):
        return self._contracts

    def authors(self):
        return list(set(contract.author for contract in self._contracts))
