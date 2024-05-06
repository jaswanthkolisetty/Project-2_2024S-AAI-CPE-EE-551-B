from Media import Media

class Book(Media):
    """
    Represents a book object, extending the Media class with specific attributes for books.

    Attributes:
        _authors (str): The authors of the book.
        _isbn (str): The standard International Standard Book Number.
        _isbn13 (str): The 13-digit ISBN.
        _language_code (str): The language code of the book.
        _num_pages (int): The number of pages in the book.
        _ratings_count (int): The number of ratings the book has received.
        _publication_date (str): The publication date of the book.
        _publisher (str): The publisher of the book.
    """
    def __init__(self, book_id, title, authors, average_rating, isbn, isbn13, language_code, num_pages, ratings_count, publication_date, publisher):
        """
        Initializes a new Book object, which is a specific type of Media.

        :param book_id: The unique identifier for the book.
        :type book_id: int
        :param title: The title of the book.
        :type title: str
        :param authors: The authors of the book.
        :type authors: str
        :param average_rating: The average rating of the book.
        :type average_rating: float
        :param isbn: The standard International Standard Book Number.
        :type isbn: str
        :param isbn13: The 13-digit ISBN.
        :type isbn13: str
        :param language_code: The language code of the book.
        :type language_code: str
        :param num_pages: The number of pages in the book.
        :type num_pages: int
        :param ratings_count: The number of ratings the book has received.
        :type ratings_count: int
        :param publication_date: The publication date of the book.
        :type publication_date: str
        :param publisher: The publisher of the book.
        :type publisher: str
        """
        super().__init__(book_id, title, average_rating)
        self._authors = authors
        self._isbn = isbn
        self._isbn13 = isbn13
        self._language_code = language_code
        self._num_pages = num_pages
        self._ratings_count = ratings_count
        self._publication_date = publication_date
        self._publisher = publisher

    def get_authors(self):
        """
        Gets the authors of the book.

        :return: The authors of the book.
        :rtype: str
        """
        return self._authors

    def set_authors(self, authors):
        """
        Sets the authors of the book.

        :param authors: The new authors of the book.
        :type authors: str
        """
        self._authors = authors

    def get_isbn(self):
        """
        Gets the ISBN of the book.

        :return: The ISBN of the book.
        :rtype: str
        """
        return self._isbn

    def set_isbn(self, isbn):
        """
        Sets the ISBN of the book.

        :param isbn: The new ISBN of the book.
        :type isbn: str
        """
        self._isbn = isbn

    def get_isbn13(self):
        """
        Gets the 13-digit ISBN of the book.

        :return: The ISBN13 of the book.
        :rtype: str
        """
        return self._isbn13

    def set_isbn13(self, isbn13):
        """
        Sets the 13-digit ISBN of the book.

        :param isbn13: The new ISBN13 of the book.
        :type isbn13: str
        """
        self._isbn13 = isbn13

    def get_language_code(self):
        """
        Gets the language code of the book.

        :return: The language code of the book.
        :rtype: str
        """
        return self._language_code

    def set_language_code(self, language_code):
        """
        Sets the language code of the book.

        :param language_code: The new language code of the book.
        :type language_code: str
        """
        self._language_code = language_code

    def get_num_pages(self):
        """
        Gets the number of pages in the book.

        :return: The number of pages in the book.
        :rtype: int
        """
        return self._num_pages

    def set_num_pages(self, num_pages):
        """
        Sets the number of pages in the book.

        :param num_pages: The new number of pages in the book.
        :type num_pages: int
        """
        self._num_pages = num_pages

    def get_ratings_count(self):
        """
        Gets the number of ratings the book has received.

        :return: The number of ratings for the book.
        :rtype: int
        """
        return self._ratings_count

    def set_ratings_count(self, ratings_count):
        """
        Sets the number of ratings the book has received.

        :param ratings_count: The new number of ratings for the book.
        :type ratings_count: int
        """
        self._ratings_count = ratings_count

    def get_publication_date(self):
        """
        Gets the publication date of the book.

        :return: The publication date of the book.
        :rtype: str
        """
        return self._publication_date

    def set_publication_date(self, publication_date):
        """
        Sets the publication date of the book.

        :param publication_date: The new publication date of the book.
        :type publication_date: str
        """
        self._publication_date = publication_date

    def get_publisher(self):
        """
        Gets the publisher of the book.

        :return: The publisher of the book.
        :rtype: str
        """
        return self._publisher

    def set_publisher(self, publisher):
        """
        Sets the publisher of the book.

        :param publisher: The new publisher of the book.
        :type publisher: str
        """
        self._publisher = publisher
