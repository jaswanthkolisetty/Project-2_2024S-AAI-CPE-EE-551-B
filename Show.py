# Team Member Names:
# 1. Karthik Samudrala
# 2. Baby Sahithi Samudrala
# 3. Jaswanth Kolisetty
# Developed on Date: May 5th, 2024
# Our Github Repository Link: https://github.com/jaswanthkolisetty/Project-2_2024S-AAI-CPE-EE-551-B.git

from Media import Media

class Show(Media):
    """
    Represents a television show or movie, extending the Media class with specific attributes for visual media.

    Attributes:
        _show_type (str): The type of the show, e.g., "Movie" or "TV Show".
        _director (str): The director of the show.
        _cast (str): List of main actors in the show.
        _country (str): Country where the show was produced.
        _date_added (str): Date when the show was added to the database or platform.
        _release_year (int): The year the show was released.
        _rating (str): The rating of the show, e.g., PG, R.
        _duration (str): The length of the show, usually in minutes or seasons.
        _listed_in (str): Categories or genres the show is listed under.
        _description (str): A brief description of the show.
    """
    def __init__(self, show_id, show_type, title, director, cast, average_rating, country, date_added, release_year, rating, duration, listed_in, description):
        """
        Initializes a new Show object, which is a specific type of Media.

        :param show_id: The unique identifier for the show.
        :type show_id: int
        :param show_type: The type of the show (e.g., 'Movie' or 'TV Show').
        :type show_type: str
        :param title: The title of the show.
        :type title: str
        :param director: The director of the show.
        :type director: str
        :param cast: The main actors involved in the show.
        :type cast: str
        :param average_rating: The average rating of the show.
        :type average_rating: float
        :param country: The country where the show was produced.
        :type country: str
        :param date_added: The date the show was added to the platform.
        :type date_added: str
        :param release_year: The year the show was released.
        :type release_year: int
        :param rating: The rating of the show (e.g., 'PG', 'R').
        :type rating: str
        :param duration: The length of the show.
        :type duration: str
        :param listed_in: The genres or categories the show is listed under.
        :type listed_in: str
        :param description: A brief description of the show.
        :type description: str
        """
        super().__init__(show_id, title, average_rating)
        self._show_type = show_type
        self._director = director
        self._cast = cast
        self._country = country
        self._date_added = date_added
        self._release_year = release_year
        self._rating = rating
        self._duration = duration
        self._listed_in = listed_in
        self._description = description

    def get_show_type(self):
        """
        Gets the type of the show.

        :return: The type of the show.
        :rtype: str
        """
        return self._show_type

    def set_show_type(self, show_type):
        """
        Sets the type of the show.

        :param show_type: The new type of the show.
        :type show_type: str
        """
        self._show_type = show_type

    def get_director(self):
        """
        Gets the director of the show.

        :return: The director of the show.
        :rtype: str
        """
        return self._director

    def set_director(self, director):
        """
        Sets the director of the show.

        :param director: The new director of the show.
        :type director: str
        """
        self._director = director

    def get_cast(self):
        """
        Gets the main actors involved in the show.

        :return: The cast of the show.
        :rtype: str
        """
        return self._cast

    def set_cast(self, cast):
        """
        Sets the main actors involved in the show.

        :param cast: The new cast of the show.
        :type cast: str
        """
        self._cast = cast

    def get_country(self):
        """
        Gets the country where the show was produced.

        :return: The country of origin of the show.
        :rtype: str
        """
        return self._country

    def set_country(self, country):
        """
        Sets the country where the show was produced.

        :param country: The new country of production for the show.
        :type country: str
        """
        self._country = country

    def get_date_added(self):
        """
        Gets the date when the show was added to the platform.

        :return: The date added.
        :rtype: str
        """
        return self._date_added

    def set_date_added(self, date_added):
        """
        Sets the date when the show was added to the platform.

        :param date_added: The new date the show was added.
        :type date_added: str
        """
        self._date_added = date_added

    def get_release_year(self):
        """
        Gets the release year of the show.

        :return: The year the show was released.
        :rtype: int
        """
        return self._release_year

    def set_release_year(self, release_year):
        """
        Sets the release year of the show.

        :param release_year: The new release year for the show.
        :type release_year: int
        """
        self._release_year = release_year

    def get_rating(self):
        """
        Gets the rating of the show.

        :return: The rating of the show.
        :rtype: str
        """
        return self._rating

    def set_rating(self, rating):
        """
        Sets the rating of the show.

        :param rating: The new rating for the show.
        :type rating: str
        """
        self._rating = rating

    def get_duration(self):
        """
        Gets the duration of the show.

        :return: The duration of the show.
        :rtype: str
        """
        return self._duration

    def set_duration(self, duration):
        """
        Sets the duration of the show.

        :param duration: The new duration of the show.
        :type duration: str
        """
        self._duration = duration

    def get_listed_in(self):
        """
        Gets the genres or categories the show is listed under.

        :return: The genres of the show.
        :rtype: str
        """
        return self._listed_in

    def set_listed_in(self, listed_in):
        """
        Sets the genres or categories the show is listed under.

        :param listed_in: The new genres or categories for the show.
        :type listed_in: str
        """
        self._listed_in = listed_in

    def get_description(self):
        """
        Gets a brief description of the show.

        :return: The description of the show.
        :rtype: str
        """
        return self._description

    def set_description(self, description):
        """
        Sets a brief description of the show.

        :param description: The new description of the show.
        :type description: str
        """
        self._description = description
