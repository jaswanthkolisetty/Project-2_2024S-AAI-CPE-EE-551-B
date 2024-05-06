class Media:
    """
    Represents a general media object with methods to manage its properties.

    Attributes:
        _media_id (int): The ID of the media item.
        _title (str): The title of the media item.
        _average_rating (float): The average rating of the media item.
    """
    def __init__(self, media_id, title, average_rating):
        """
        Initializes a new Media object.

        :param media_id: The unique identifier for the media.
        :type media_id: int
        :param title: The title of the media.
        :type title: str
        :param average_rating: The average rating of the media.
        :type average_rating: float
        """
        self._media_id = media_id        # Protected member variable for media ID
        self._title = title              # Protected member variable for media title
        self._average_rating = average_rating  # Protected member variable for media rating

    def get_media_id(self):
        """
        Gets the media ID.

        :return: The media ID.
        :rtype: int
        """
        return self._media_id

    def set_media_id(self, media_id):
        """
        Sets a new media ID.

        :param media_id: The new media ID to set.
        :type media_id: int
        """
        self._media_id = media_id

    def get_title(self):
        """
        Gets the title of the media.

        :return: The title of the media.
        :rtype: str
        """
        return self._title

    def set_title(self, title):
        """
        Sets a new title for the media.

        :param title: The new title to set.
        :type title: str
        """
        self._title = title

    def get_average_rating(self):
        """
        Gets the average rating of the media.

        :return: The average rating of the media.
        :rtype: float
        """
        return self._average_rating

    def set_average_rating(self, average_rating):
        """
        Sets a new average rating for the media.

        :param average_rating: The new average rating to set.
        :type average_rating: float
        """
        self._average_rating = average_rating
