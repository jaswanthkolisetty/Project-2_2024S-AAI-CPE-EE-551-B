import csv
import tkinter as tk
from tkinter import filedialog
from Book import Book
from Show import Show
import collections
from tkinter import messagebox


class Recommender:
    def __init__(self):
        self.books = {}  # Dictionary to store Book objects
        self.shows = {}  # Dictionary to store Show objects
        self.associations = {}  # Nested dictionaries to store associations

    def loadBooks(self):
        filename = filedialog.askopenfilename()
        if not filename:
            print("No file selected.")
            return
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=',')  # Changed delimiter to ','
            self.books = {}
            for row in reader:
                # Convert data types if necessary
                book = Book(
                    book_id=int(row['bookID']),  # Assuming book_id is an integer
                    title=row['title'],
                    authors=row['authors'],
                    average_rating=float(row['average_rating']),  # Convert to float
                    isbn=row['isbn'],
                    isbn13=row['isbn13'],
                    language_code=row['language_code'],
                    num_pages=int(row['num_pages']),  # Convert to integer
                    ratings_count=int(row['ratings_count']),  # Convert to integer
                    publication_date=row['publication_date'],
                    publisher=row['publisher']
                )
                self.books[int(row['bookID'])] = book  # Assuming book_id is an integer
        print("Books loaded successfully.")

    def loadShows(self):
        filename = filedialog.askopenfilename()
        if not filename:
            print("No file selected.")
            return

        # Assuming the file might have a header issue, try to detect the delimiter
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            sample = file.read(1024)
            print(sample)
            sniffer = csv.Sniffer()
            dialect = sniffer.sniff(sample)

        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=dialect.delimiter)
            self.shows = {}
            for row in reader:
                print(row)
                show = Show(
                    show_id=row['show_id'],
                    show_type=row['type'],
                    title=row['title'],
                    director=row['director'],
                    cast=row['cast'].replace('\\', ', '),  # Assuming the cast is split by backslashes
                    average_rating=row['average_rating'],
                    country=row['country'],
                    date_added=row['date_added'],
                    release_year=row['release_year'],
                    rating=row['rating'],
                    duration=row['duration'],
                    listed_in=row['listed_in'].replace('\\', ', '),  # Assuming the genres are split by backslashes
                    description=row['description']
                )
                self.shows[row['show_id']] = show
        print("Shows loaded successfully.")

    def loadAssociations(self):
        filename = filedialog.askopenfilename()
        if not filename:
            print("No file selected.")
            return
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            self.associations = {}
            for row in reader:
                print(row)
                id1, id2 = row[0], row[1]
                if id1 not in self.associations:
                    self.associations[id1] = {}
                if id2 not in self.associations[id1]:
                    self.associations[id1][id2] = 0
                self.associations[id1][id2] += 1

                # Reverse association
                if id2 not in self.associations:
                    self.associations[id2] = {}
                if id1 not in self.associations[id2]:
                    self.associations[id2][id1] = 0
                self.associations[id2][id1] += 1
        print("Associations loaded successfully.")

    def getMovieList(self):
        # Collect movie titles and durations, ensuring the show type is 'movie'
        movies = [(show._title, show._duration) for show in self.shows.values() if show._show_type.lower() == 'movie']

        # Determine the maximum length of titles and durations for formatting
        if movies:
            max_title_length = max(len(title) for title, _ in movies)
            max_duration_length = max(len(duration) for _, duration in movies)
        else:
            max_title_length = max_duration_length = 0

        # Prepare output
        output_lines = []

        # Create a formatted header
        header = f"{'Title'.ljust(max_title_length + 2)} {'Duration'}"
        output_lines.append(header)

        # Format each movie title and duration into the output
        for title, duration in movies:
            formatted_line = f"{title.ljust(max_title_length + 2)} {duration}"
            output_lines.append(formatted_line)

        return output_lines

    def getTVList(self):
        # Collect titles and durations (as seasons) for TV shows
        tv_shows = [(show._title, show._duration) for show in self.shows.values() if
                    show._show_type.lower() == 'tv show']

        # Determine the maximum length of titles and durations (seasons) for formatting
        if tv_shows:
            max_title_length = max(len(title) for title, _ in tv_shows)
            max_seasons_length = max(len(season) for _, season in tv_shows)
        else:
            max_title_length = max_seasons_length = 0

        # Prepare output
        output_lines = []

        # Create a formatted header
        header = f"{'Title'.ljust(max_title_length + 2)} {'Seasons'}"
        output_lines.append(header)

        # Format each TV show's title and duration (season) into the output
        for title, seasons in tv_shows:
            formatted_line = f"{title.ljust(max_title_length + 2)} {seasons}"
            output_lines.append(formatted_line)

        return output_lines

    def getBookList(self):
        # Collect titles and authors for books
        books = [(book._title, book._authors) for book in self.books.values()]

        # Determine the maximum length of titles and authors for formatting
        if books:
            max_title_length = max(len(title) for title, _ in books)
            max_authors_length = max(len(authors) for _, authors in books)
        else:
            max_title_length = max_authors_length = 0

        # Prepare output
        output_lines = []

        # Create a formatted header
        header = f"{'Title'.ljust(max_title_length + 2)} {'Authors'}"
        output_lines.append(header)

        # Format each book's title and authors into the output
        for title, authors in books:
            formatted_line = f"{title.ljust(max_title_length + 2)} {authors}"
            output_lines.append(formatted_line)

        return output_lines

    import collections

    def getMovieStats(self):
        # Collect data for movies only
        movies = [show for show in self.shows.values() if show._show_type.lower() == 'movie']

        # Rating distributions and calculation of percentages
        ratings = [movie._rating for movie in movies]
        rating_count = collections.Counter(ratings)
        total_ratings = sum(rating_count.values())
        rating_percentages = {rating: f"{(count / total_ratings * 100):.2f}%" for rating, count in rating_count.items()}

        # Calculate average movie duration
        durations = [int(duration.replace(' min', '')) for movie in movies for duration in movie._duration.split() if
                     duration.isdigit()]
        average_duration = sum(durations) / len(durations) if durations else 0

        # Find the most frequent director
        directors = [movie._director for movie in movies if movie._director]
        most_frequent_director = collections.Counter(directors).most_common(1)[0][0] if directors else 'None'

        # Find the most frequent actor
        actors = [actor.strip() for movie in movies for actor in movie._cast.split(',') if movie._cast]
        most_frequent_actor = collections.Counter(actors).most_common(1)[0][0] if actors else 'None'

        # Find the most frequent genre
        genres = [genre.strip() for movie in movies for genre in movie._listed_in.split(',') if movie._listed_in]
        most_frequent_genre = collections.Counter(genres).most_common(1)[0][0] if genres else 'None'

        # Return all stats
        return {
            'Rating Percentages': rating_percentages,
            'Average Duration (min)': f"{average_duration:.2f}",
            'Most Frequent Director': most_frequent_director,
            'Most Frequent Actor': most_frequent_actor,
            'Most Frequent Genre': most_frequent_genre
        }


    def getTVStats(self):
        # Filter to get only TV shows
        tv_shows = [show for show in self.shows.values() if show._show_type.lower() == 'tv show']

        # Rating distributions and calculation of percentages
        ratings = [show._rating for show in tv_shows if show._rating]
        rating_count = collections.Counter(ratings)
        total_ratings = sum(rating_count.values())
        rating_percentages = {rating: f"{(count / total_ratings * 100):.2f}%" for rating, count in rating_count.items()}

        # Calculate average number of seasons (assuming the duration field holds season info and is formatted as "N Seasons")
        seasons = [int(season.split()[0]) for show in tv_shows for season in show._duration.split() if
                   season.split()[0].isdigit()]
        average_seasons = sum(seasons) / len(seasons) if seasons else 0

        # Most frequent actor in TV shows
        actors = [actor.strip() for show in tv_shows for actor in show._cast.split(',') if show._cast]
        most_frequent_actor = collections.Counter(actors).most_common(1)[0][0] if actors else 'None'

        # Most frequent TV show genre
        genres = [genre.strip() for show in tv_shows for genre in show._listed_in.split(',') if show._listed_in]
        most_frequent_genre = collections.Counter(genres).most_common(1)[0][0] if genres else 'None'

        # Return all stats as a dictionary
        return {
            'Rating Percentages': rating_percentages,
            'Average Number of Seasons': f"{average_seasons:.2f}",
            'Most Frequent Actor': most_frequent_actor,
            'Most Frequent Genre': most_frequent_genre
        }

    import collections

    def getBookStats(self):
        # Ensure that books are loaded
        if not self.books:
            return "No books are loaded in the system."

        # Calculate average page count
        page_counts = [int(book._num_pages) for book in self.books.values()]
        average_page_count = sum(page_counts) / len(page_counts) if page_counts else 0

        # Most frequent author
        authors = [author.strip() for book in self.books.values() for author in book._authors.split(',')]
        author_count = collections.Counter(authors)
        most_frequent_author = author_count.most_common(1)[0][0] if authors else 'None'

        # Most frequent publisher
        publishers = [book._publisher for book in self.books.values() if book._publisher]
        publisher_count = collections.Counter(publishers)
        most_frequent_publisher = publisher_count.most_common(1)[0][0] if publishers else 'None'

        # Return all stats as a dictionary
        return {
            'Average Page Count': f"{average_page_count:.2f}",
            'Most Frequent Author': most_frequent_author,
            'Most Frequent Publisher': most_frequent_publisher
        }


    def searchTVMovies(self, media_type, title='', director='', actor='', genre=''):
        root = tk.Tk()
        root.withdraw()  # Hides the main window

        # Validate media type
        if media_type.lower() not in ['movie', 'tv show']:
            messagebox.showerror("Error", "Please select 'Movie' or 'TV Show' from Type first.")
            return "No Results"

        # Check if all search fields are empty
        if not any([title, director, actor, genre]):
            messagebox.showerror("Error", "Please enter information for Title, Director, Actor, and/or Genre first.")
            return "No Results"

        # Filter shows based on input criteria
        filtered_shows = [
            show for show in self.shows.values()
            if show._show_type.lower() == media_type.lower() and
               (title.lower() in show._title.lower() if title else True) and
               (director.lower() in show._director.lower() if director and show._director else True) and
               (actor.lower() in show._cast.lower() if actor and show._cast else True) and
               (genre.lower() in show._listed_in.lower() if genre and show._listed_in else True)
        ]

        # Determine the maximum length of each column for formatting
        if filtered_shows:
            max_title_length = max(len(show._title) for show in filtered_shows)
            max_director_length = max(len(show._director) for show in filtered_shows if show._director)
            max_actor_length = max(len(show._cast) for show in filtered_shows if show._cast)
            max_genre_length = max(len(show._listed_in) for show in filtered_shows if show._listed_in)

            # Create header
            header = f"{'Title'.ljust(max_title_length)} {'Director'.ljust(max_director_length)} {'Actors'.ljust(max_actor_length)} {'Genre'.ljust(max_genre_length)}"
            output = [header]

            # Format each show into the output
            for show in filtered_shows:
                line = f"{show._title.ljust(max_title_length)} {show._director.ljust(max_director_length)} {show._cast.ljust(max_actor_length)} {show._listed_in.ljust(max_genre_length)}"
                output.append(line)

            return '\n'.join(output)
        else:
            return "No Results"

    def searchBooks(self, title='', author='', publisher=''):
        root = tk.Tk()
        root.withdraw()  # Hides the main window

        # Check if all search fields are empty
        if not any([title, author, publisher]):
            messagebox.showerror("Error", "Please enter information for Title, Author, and/or Publisher first.")
            return "No Results"

        # Filter books based on input criteria
        filtered_books = [
            book for book in self.books.values()
            if (title.lower() in book._title.lower() if title else True) and
               (author.lower() in book._authors.lower() if author else True) and
               (publisher.lower() in book._publisher.lower() if publisher else True)
        ]

        # Determine the maximum length of each column for formatting
        if filtered_books:
            max_title_length = max(len(book._title) for book in filtered_books)
            max_authors_length = max(len(book._authors) for book in filtered_books)
            max_publisher_length = max(len(book._publisher) for book in filtered_books)

            # Create header
            header = f"{'Title'.ljust(max_title_length)} {'Author'.ljust(max_authors_length)} {'Publisher'.ljust(max_publisher_length)}"
            output = [header]

            # Format each book into the output
            for book in filtered_books:
                line = f"{book._title.ljust(max_title_length)} {book._authors.ljust(max_authors_length)} {book._publisher.ljust(max_publisher_length)}"
                output.append(line)

            return '\n'.join(output)
        else:
            return "No Results"

    def getRecommendations(self, media_type, title):
        root = tk.Tk()
        root.withdraw()  # Hides the main window

        # Handle recommendations for Movies or TV Shows
        if media_type.lower() in ['movie', 'tv show']:
            # Find the ID associated with the title
            media_id = next((show_id for show_id, show in self.shows.items()
                             if show._title.lower() == title.lower() and show._show_type.lower() == media_type.lower()),
                            None)

            if not media_id:
                messagebox.showwarning("Warning", f"There are no recommendations for the title '{title}'.")
                return "No results"

            # Find all book associations for this media ID
            if media_id in self.associations:
                associated_books = self.associations[media_id]
                book_details = []

                for book_id in associated_books:
                    if book_id in self.books:
                        book = self.books[book_id]
                        book_details.append(
                            f"Title: {book._title}, Author: {book._authors}, Publisher: {book._publisher}")

                if book_details:
                    return "\n".join(book_details)
                else:
                    return "No results"
            else:
                return "No results"

        # Add additional branches if handling other types (like books) for recommendations
        else:
            messagebox.showwarning("Warning", "Please select 'Movie' or 'TV Show' as type.")
            return "No results"

    def getRecommendations(self, media_type, title):
        root = tk.Tk()
        root.withdraw()  # Hides the main window

        results = "No results"
        if media_type.lower() in ['movie', 'tv show']:
            # Search for Movies or TV Shows
            media_id = next((id for id, show in self.shows.items()
                             if show._title.lower() == title.lower() and show._show_type.lower() == media_type.lower()),
                            None)
            if not media_id:
                messagebox.showwarning("Warning", f"No recommendations found for the title '{title}'.")
            else:
                # Look for associated books
                associated_items = self.associations.get(media_id, {})
                if associated_items:
                    book_details = [
                        f"Title: {self.books[book_id]._title}, Author: {self.books[book_id]._authors}, Publisher: {self.books[book_id]._publisher}"
                        for book_id in associated_items if book_id in self.books]
                    if book_details:
                        results = "\n".join(book_details)

        elif media_type.lower() == 'book':
            # Search for Books
            book_id = next((id for id, book in self.books.items() if book._title.lower() == title.lower()), None)
            if not book_id:
                messagebox.showwarning("Warning", f"No recommendations found for the title '{title}'.")
            else:
                # Look for associated movies or TV shows
                associated_items = self.associations.get(book_id, {})
                if associated_items:
                    show_details = [
                        f"Title: {self.shows[show_id]._title}, Director: {self.shows[show_id]._director}, Actors: {self.shows[show_id]._cast}, Genre: {self.shows[show_id]._listed_in}"
                        for show_id in associated_items if show_id in self.shows]
                    if show_details:
                        results = "\n".join(show_details)

        else:
            messagebox.showwarning("Warning",
                                   "Invalid media type provided. Please select 'Movie', 'TV Show', or 'Book'.")

        return results
