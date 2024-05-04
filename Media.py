class Media:
    def __init__(self, media_id, title, average_rating):
        self._media_id = media_id        # Protected member variable
        self._title = title              # Protected member variable
        self._average_rating = average_rating  # Protected member variable

    # Accessor for media_id
    def get_media_id(self):
        return self._media_id

    # Mutator for media_id
    def set_media_id(self, media_id):
        self._media_id = media_id

    # Accessor for title
    def get_title(self):
        return self._title

    # Mutator for title
    def set_title(self, title):
        self._title = title

    # Accessor for average_rating
    def get_average_rating(self):
        return self._average_rating

    # Mutator for average_rating
    def set_average_rating(self, average_rating):
        self._average_rating = average_rating
