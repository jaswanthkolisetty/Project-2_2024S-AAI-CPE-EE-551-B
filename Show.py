from Media import Media

class Show(Media):
    def __init__(self, show_id, show_type, title, director, cast, average_rating, country, date_added, release_year, rating, duration, listed_in, description):
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
        return self._show_type

    def set_show_type(self, show_type):
        self._show_type = show_type

    def get_directors(self):
        return self._directors

    def set_directors(self, directors):
        self._directors = directors

    def get_cast(self):
        return self._cast

    def set_cast(self, cast):
        self._cast = cast

    def get_country(self):
        return self._country

    def set_country(self, country):
        self._country = country

    def get_date_added(self):
        return self._date_added

    def set_date_added(self, date_added):
        self._date_added = date_added

    def get_release_year(self):
        return self._release_year

    def set_release_year(self, release_year):
        self._release_year = release_year

    def get_rating(self):
        return self._rating

    def set_rating(self, rating):
        self._rating = rating

    def get_duration(self):
        return self._duration

    def set_duration(self, duration):
        self._duration = duration

    def get_genres(self):
        return self._genres

    def set_genres(self, genres):
        self._genres = genres

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description
