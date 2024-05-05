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
        while True:
            filename = filedialog.askopenfilename()  # This opens the file dialog
            if not filename:
                if messagebox.askretrycancel("Retry", "No file selected. Try again?"):
                    continue
                else:
                    print("No file selected, and user cancelled the operation.")
                    return
            break
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
        print(self.books[31851]._title)

    def loadShows(self):
        while True:
            filename = filedialog.askopenfilename()  # This opens the file dialog
            if not filename:
                if messagebox.askretrycancel("Retry", "No file selected. Try again?"):
                    continue
                else:
                    print("No file selected, and user cancelled the operation.")
                    return
            break

        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=',')  # Explicitly specify delimiter
            self.shows = {}
            for row in reader:
                print(row)
                show = Show(
                    show_id=row['show_id'],
                    show_type=row['type'],
                    title=row['title'],
                    director=row['director'],
                    cast=row['cast'].replace('\\', '\\'),
                    average_rating=row['average_rating'],
                    country=row['country'],
                    date_added=row['date_added'],
                    release_year=row['release_year'],
                    rating=row['rating'],
                    duration=row['duration'],
                    listed_in=row['listed_in'].replace('\\', '\\'),
                    description=row['description']
                )
                self.shows[row['show_id']] = show
        print("Shows loaded successfully.")


    def loadAssociations(self):
        while True:
            filename = filedialog.askopenfilename()  # This opens the file dialog
            if not filename:
                if messagebox.askretrycancel("Retry", "No file selected. Try again?"):
                    continue
                else:
                    print("No file selected, and user cancelled the operation.")
                    return
            break

        try:
            with open(filename, 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file, delimiter=',')
                for row in reader:
                    if len(row) < 2:  # Ensure there are at least two IDs per row
                        continue  # Skip rows that don't have at least two IDs

                    id1, id2 = row[0].strip(), row[1].strip()  # Strip spaces which could cause key mismatch
                    for a, b in [(id1, id2), (id2, id1)]:  # Process both (id1, id2) and (id2, id1)
                        if a not in self.associations:
                            self.associations[a] = {}
                        if b not in self.associations[a]:
                            self.associations[a][b] = 0
                        self.associations[a][b] += 1
            print("Associations loaded successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read file: {e}")

    def getMovieList(self):
        # Collect movie titles and durations, ensuring the show type is 'movie'
        movies = [(show._title, show._duration) for show in self.shows.values() if show._show_type.lower() == 'movie']
        if not movies:
            return
        # Determine the maximum length of titles and durations for formatting
        if movies:
            max_title_length = max(len(title) for title, _ in movies)
            max_duration_length = max(len(duration) for _, duration in movies)
        else:
            max_title_length = max_duration_length = 0

        # Prepare output
        output_lines = []

        # Create a formatted header
        header = f"{'Title'.ljust(max_title_length + 2)} {'Runtime'}"
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
        if not books:
            return
        # Determine the maximum length of titles and authors for formatting
        if books:
            max_title_length = max(len(title) for title, _ in books)
            max_authors_length = max(len(authors) for _, authors in books)
        else:
            max_title_length = max_authors_length = 0

        # Prepare output
        output_lines = []

        # Create a formatted header
        header = f"{'Title'.ljust(max_title_length + 2)} {'Author(s)'}"
        output_lines.append(header)

        # Format each book's title and authors into the output
        for title, authors in books:
            formatted_line = f"{title.ljust(max_title_length + 2)} {authors}"
            output_lines.append(formatted_line)

        return output_lines


    def getMovieStats(self):
        # Collect data for movies only
        movies = [show for show in self.shows.values() if show._show_type.lower() == 'movie']
        if not movies:
            return "No movies found."

        # Rating distributions and calculation of percentages
        ratings = [movie._rating for movie in movies]
        rating_count = collections.Counter(ratings)
        total_ratings = sum(rating_count.values())
        rating_percentages = {rating: f"{(count / total_ratings * 100):.2f}%" for rating, count in rating_count.items()}

        # Format ratings percentages
        formatted_ratings = "\n".join(
            [f"{rating if rating else 'None'} {percent}" for rating, percent in rating_percentages.items()])

        # Calculate average movie duration
        durations = [int(movie._duration.replace(' min', '')) for movie in movies if 'min' in movie._duration]
        average_duration = sum(durations) / len(durations) if durations else 0

        # Find the most frequent director
        directors = [movie._director for movie in movies if movie._director]
        most_frequent_director = collections.Counter(directors).most_common(1)[0][0] if directors else 'None'

        # Find the most frequent actor
        actors = [actor.strip() for movie in movies for actor in movie._cast.split('\\') if movie._cast]
        most_frequent_actor = collections.Counter(actors).most_common(1)[0][0] if actors else 'None'

        # Find the most frequent genre
        genres = [genre.strip() for movie in movies for genre in movie._listed_in.split('\\') if movie._listed_in]
        most_frequent_genre = collections.Counter(genres).most_common(1)[0][0] if genres else 'None'

        # Compile all stats into a formatted string
        stats = (
                "Ratings:\n" + formatted_ratings + "\n\n" +
                f"Average Movie Duration: {average_duration:.2f} minutes\n\n" +
                f"Most Prolific Director: {most_frequent_director}\n\n" +
                f"Most Prolific Actor: {most_frequent_actor}\n\n" +
                f"Most Frequent Genre: {most_frequent_genre}"
        )

        return stats


    def getTVStats(self):
        # Filter to get only TV shows
        tv_shows = [show for show in self.shows.values() if show._show_type.lower() == 'tv show']

        # Rating distributions and calculation of percentages
        ratings = [show._rating for show in tv_shows if show._rating]
        rating_count = collections.Counter(ratings)
        total_ratings = sum(rating_count.values())
        rating_percentages = {rating: f"{(count / total_ratings * 100):.2f}%" for rating, count in rating_count.items()}

        # Format ratings percentages
        formatted_ratings = "Ratings:\n" + "\n".join(
            [f"{rating if rating else 'None'} {percent}" for rating, percent in rating_percentages.items()])

        # Calculate average number of seasons (assuming the duration field holds season info and is formatted as "N Seasons")
        seasons = [int(season.split()[0]) for show in tv_shows for season in show._duration.split() if
                   season.split()[0].isdigit()]
        average_seasons = sum(seasons) / len(seasons) if seasons else 0
        average_seasons_formatted = f"Average Number of Seasons: {average_seasons:.2f} seasons"

        # Most frequent actor in TV shows
        actors = [actor.strip() for show in tv_shows for actor in show._cast.split('\\') if show._cast]
        most_frequent_actor = collections.Counter(actors).most_common(1)[0][0] if actors else 'None'
        most_frequent_actor_formatted = f"Most Prolific Actor: {most_frequent_actor}"

        # Most frequent TV show genre
        genres = [genre.strip() for show in tv_shows for genre in show._listed_in.split('\\') if show._listed_in]
        most_frequent_genre = collections.Counter(genres).most_common(1)[0][0] if genres else 'None'
        most_frequent_genre_formatted = f"Most Frequent Genre: {most_frequent_genre}"

        # Combine all stats into a single formatted string
        stats_summary = f"{formatted_ratings}\n\n{average_seasons_formatted}\n\n{most_frequent_actor_formatted}\n\n{most_frequent_genre_formatted}"
        return stats_summary

    def getBookStats(self):
        # Ensure that books are loaded
        if not self.books:
            return "No books are loaded in the system."

        # Calculate average page count
        page_counts = [int(book._num_pages) for book in self.books.values()]
        average_page_count = sum(page_counts) / len(page_counts) if page_counts else 0
        average_page_count_formatted = f"Average Page Count: {average_page_count:.2f} pages"

        # Most frequent author
        authors = [author.strip() for book in self.books.values() for author in book._authors.split('\\')]
        author_count = collections.Counter(authors)
        most_frequent_author = author_count.most_common(1)[0][0] if authors else 'None'
        most_frequent_author_formatted = f"Most Prolific Author: {most_frequent_author}"

        # Most frequent publisher
        publishers = [book._publisher for book in self.books.values() if book._publisher]
        publisher_count = collections.Counter(publishers)
        most_frequent_publisher = publisher_count.most_common(1)[0][0] if publishers else 'None'
        most_frequent_publisher_formatted = f"Most Prolific Publisher: {most_frequent_publisher}"

        stats_summary = f"{average_page_count_formatted}\n\n{most_frequent_author_formatted}\n\n{most_frequent_publisher_formatted}"
        return stats_summary

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
            try:
                max_title_length = max((len(show._title) for show in filtered_shows), default=0)
                max_director_length = max((len(show._director) for show in filtered_shows if show._director), default=0)
                max_actor_length = max((len(show._cast) for show in filtered_shows if show._cast), default=0)
                max_genre_length = max((len(show._listed_in) for show in filtered_shows if show._listed_in), default=0)

                print(max_title_length,max_director_length,max_actor_length,max_genre_length)
                # Create header
                header = f"{'Title'.ljust(max_title_length)} {'Director'.ljust(max_director_length)} {'Actor'.ljust(max_actor_length)} {'Genre'.ljust(max_genre_length)}"
                output = [header]

                # Format each show into the output
                for show in filtered_shows:
                    line = f"{(show._title or '').ljust(max_title_length) if max_title_length > 0 else ' '*5} {(show._director or '').ljust(max_director_length) if max_director_length > 0 else ' '*8} {(show._cast or '').ljust(max_actor_length) if max_actor_length > 0 else ' '*5} {(show._listed_in or '').ljust(max_genre_length) if max_genre_length > 0 else ' '*5}"
                    output.append(line)

                return '\n'.join(output)
            except ValueError as e:
                print(e)
                return "No Results"
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
        if media_type.lower() in ['movie', 'tv show']:
            media_id = next((id for id, show in self.shows.items() if
                             show._title.lower() == title.lower() and show._show_type.lower() == media_type.lower()),
                            None)

            if not media_id:
                messagebox.showwarning("Warning", f"No recommendations found for the title '{title}'.")
                return "No results"

            # Fetch associated books
            associated_items = self.associations.get(media_id, {})
            if not associated_items:
                return "No associated books found."

            book_details = "\n".join([
                f"Title:\n{self.books[int(book_id)]._title}\n"
                f"Author:\n{self.books[int(book_id)]._authors}\n"
                f"Average Rating:\n{self.books[int(book_id)]._average_rating}\n"
                f"ISBN:\n{self.books[int(book_id)]._isbn}\n"
                f"ISBN13:\n{self.books[int(book_id)]._isbn13}\n"
                f"Language Code:\n{self.books[int(book_id)]._language_code}\n"
                f"Pages:\n{self.books[int(book_id)]._num_pages}\n"
                f"Rating Count:\n{self.books[int(book_id)]._ratings_count}\n"
                f"Publication Date:\n{self.books[int(book_id)]._publication_date}\n"
                f"Publisher:\n{self.books[int(book_id)]._publisher}\n"
                f"\n{'*' * 50}\n"
                for book_id in associated_items if int(book_id) in self.books])

            return book_details.strip() if book_details else "No results"

        elif media_type.lower() == 'book':
            book_id = next((id for id, book in self.books.items() if book._title.lower() == title.lower()), None)
            if not book_id:
                messagebox.showwarning("Warning", f"No recommendations found for the title '{title}'.")
                return "No results"

            # Fetch associated movies or TV shows
            associated_items = self.associations.get(book_id, {})
            if not associated_items:
                return "No associated movies or TV shows found."

            show_details = "\n".join([
                f"Type:\n{self.shows[show_id]._show_type}\n"
                f"Title:\n{self.shows[show_id]._title}\n"
                f"Director:\n{self.shows[show_id]._director}\n"
                f"Cast:\n{self.shows[show_id]._cast}\n"
                f"Average Rating:\n{self.shows[show_id]._average_rating}\n"
                f"Country:\n{self.shows[show_id]._country}\n"
                f"Date Added:\n{self.shows[show_id]._date_added}\n"
                f"Release Year:\n{self.shows[show_id]._release_year}\n"
                f"Rating:\n{self.shows[show_id]._rating}\n"
                f"Duration:\n{self.shows[show_id]._duration}\n"
                f"Listed In:\n{self.shows[show_id]._listed_in}\n"
                f"Description:\n{self.shows[show_id]._description}\n"
                f"{'*' * 50}"
                for show_id in associated_items if show_id in self.shows])

            return show_details.strip() if show_details else "No results"

        else:
            messagebox.showwarning("Warning",
                                   "Invalid media type provided. Please select 'Movie', 'TV Show', or 'Book'.")
            return "No results"


