# test_many_to_many.py
import pytest
from many_to_many import Contract, Author, Book  # Import the classes

def test_contract_validates_author():
    """Test Contract class validates author of type Author"""
    book = Book("Title")
    date = '01/01/2001'
    royalties = 40000

    with pytest.raises(Exception):
        Contract("Not an Author", book, date, royalties)

def test_contract_validates_book():
    """Test Contract class validates book of type Book"""
    author = Author("Name")
    date = '01/01/2001'
    royalties = 40000

    with pytest.raises(Exception):
        Contract(author, "Not a Book", date, royalties)

def test_contract_validates_date():
    """Test Contract class validates date of type str"""
    author = Author("Name")
    book = Book("Title")
    royalties = 40000

    with pytest.raises(Exception):
        Contract(author, book, 12345, royalties)

def test_contract_validates_royalties():
    """Test Contract class validates royalties of type int"""
    author = Author("Name")
    book = Book("Title")
    date = '01/01/2001'

    with pytest.raises(Exception):
        Contract(author, book, date, "Not an int")

def test_author_has_contracts():
    """Test Author class has method contracts() that returns a list of its contracts"""
    author = Author("Name")
    book = Book("Title")
    contract = Contract(author, book, '01/01/2001', 50000)

    assert author.contracts() == [contract]

def test_author_has_books():
    """Test Author class has method books() that returns a list of its books"""
    author = Author("Name")
    book = Book("Title")
    Contract(author, book, '01/01/2001', 50000)

    assert book in author.books()

def test_book_has_contracts():
    """Test Book class has method contracts() that returns a list of its contracts"""
    author = Author("Name")
    book = Book("Title")
    contract = Contract(author, book, '01/01/2001', 50000)

    assert book.contracts() == [contract]

def test_book_has_authors():
    """Test Book class has method authors() that returns a list of its authors"""
    author = Author("Name")
    book = Book("Title")
    Contract(author, book, '01/01/2001', 50000)

    assert author in book.authors()

def test_author_has_total_royalties():
    """Test Author class has method total_royalties that gets the sum of all its related contracts' royalties"""
    author = Author("Name")
    book1 = Book("Title 1")
    book2 = Book("Title 2")
    book3 = Book("Title 3")

    Contract(author, book1, "01/01/2001", 10)
    Contract(author, book2, "01/01/2001", 20)
    Contract(author, book3, "01/01/2001", 30)

    assert author.total_royalties() == 60

def test_contract_contracts_by_date():
    """Test Contract class has method contracts_by_date() that retrieves contracts by date"""
    Contract.all_contracts.clear()  # Clear previous contracts
    author1 = Author("Name 1")
    book1 = Book("Title 1")
    book2 = Book("Title 2")
    book3 = Book("Title 3")
    author2 = Author("Name 2")
    book4 = Book("Title 4")

    contract1 = Contract(author1, book1, "02/01/2001", 10)
    contract2 = Contract(author1, book2, "01/01/2001", 20)
    contract3 = Contract(author1, book3, "03/01/2001", 30)
    contract4 = Contract(author2, book4, "01/01/2001", 40)

    assert Contract.contracts_by_date('01/01/2001') == [contract2, contract4]
