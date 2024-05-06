# Team Member Names:
# 1. Karthik Samudrala
# 2. Baby Sahithi Samudrala
# 3. Jaswanth Kolisetty
# Developed on Date: May 5th, 2024
# Our Github Repository Link: https://github.com/jaswanthkolisetty/Project-2_2024S-AAI-CPE-EE-551-B.git
# Description: Creates a graphical user interface for managing and displaying media information such as movies, TV shows, and books.
#     This GUI uses tkinter for the interface and matplotlib for rendering pie charts.

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from Recommender import Recommender
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import collections

class RecommenderGUI:
    """
    A class that creates a graphical user interface for managing and displaying media information such as movies, TV shows, and books.
    This GUI uses tkinter for the interface and matplotlib for rendering pie charts.
    """

    def __init__(self):
        """
        Initializes the RecommenderGUI class by setting up the main window, adding tabs for different media types, and adding navigation buttons.
        """
        self.recommender = Recommender()  # Instance of the Recommender class to manage the backend data.

        # Setup the main application window
        self.root = tk.Tk()
        self.root.title("Media Recommender")  # Setting Title of the main window
        self.root.geometry("1200x800")  # Setting Size of the main window
        self.root.state('zoomed')

        # Creating a Notebook widget to manage the tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both')  # Packing to make the notebook expandable and fill the window

        # This will calls to create various tabs
        self.create_movie_tab()
        self.create_tv_show_tab()
        self.create_book_tab()
        self.create_search_tab()
        self.create_search_books_tab()
        self.create_recommendation_tab()
        self.create_ratings_tab()

        # Creating navigation buttons at the bottom of the GUI
        self.create_bottom_buttons()

    def create_ratings_tab(self):
        """
        Creating a tab within the main window for displaying rating statistics in pie chart format.
        This tab will have separate frames for movies and TV shows.
        """
        self.ratings_tab = ttk.Frame(self.notebook)  # Main frame for the ratings tab
        self.notebook.add(self.ratings_tab, text="Ratings")  # Add the ratings tab to the notebook
        self.movies_frame = ttk.Frame(self.ratings_tab)  # Frame for movie ratings
        self.tv_shows_frame = ttk.Frame(self.ratings_tab)  # Frame for TV show ratings
        self.movies_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)  # Position and fill settings for movie frame
        self.tv_shows_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)  # Position and fill settings for TV show frame

        self.update_ratings_charts()  # Call the method to populate the charts initially

    def update_ratings_charts(self):
        """
        Visualizing the pie charts for movie and TV show ratings based on current data.
        This method clears existing charts and repopulates them with updated data.
        """
        # Clearing the existing widgets from the frames to ensure charts are not duplicated
        for widget in self.movies_frame.winfo_children():
            widget.destroy()
        for widget in self.tv_shows_frame.winfo_children():
            widget.destroy()

        # Creating and displaying pie charts for each show type
        for show_type, frame, title in [('movie', self.movies_frame, "Movie Ratings"),
                                        ('tv show', self.tv_shows_frame, "TV Show Ratings")]:
            shows = [show for show in self.recommender.shows.values() if show._show_type.lower() == show_type]
            if not shows:  # Checking if there are no shows of this type to display
                ttk.Label(frame, text="No data available").pack()  # Display a placeholder label
                continue  # Skiping to the next show type

            ratings = [show._rating for show in shows]  # Listing of ratings from shows
            rating_count = collections.Counter(ratings)  # Counting of each rating
            total = sum(rating_count.values())  # Total ratings for calculating percentages
            labels = list(rating_count.keys())  # Labels for the pie chart
            sizes = [(count / total) * 100 for count in rating_count.values()]  # Percentages for the pie chart

            # Checking if there is data to plot
            if labels and sizes:
                fig = Figure(figsize=(6, 5), dpi=100)  # Creating a figure for the pie chart
                subplot = fig.add_subplot(111)  # Adding a subplot to the figure
                explode = [0.1 if i == max(sizes) else 0 for i in sizes]  # Exploding the largest segment for emphasis
                # Plot the pie chart
                wedges, texts, autotexts = subplot.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90,
                                                       explode=explode, shadow=True, labeldistance=1.2)
                for text in texts:
                    text.set_color('blue')  # Seting the color of labels if needed
                subplot.axis('equal')  # Ensuring the pie chart is a circle
                subplot.set_title(title)  # Setting the title for the pie chart

                chart = FigureCanvasTkAgg(fig, master=frame)  # Creating a canvas for the figure in the Tkinter frame
                chart.draw()  # Draw the chart
                chart.get_tk_widget().pack(fill=tk.BOTH, expand=True)  # Packing the widget to make it visible

    def create_movie_tab(self):
        """
        Creates a tab specifically for movie data and statistics.
        """
        self.movie_tab = ttk.Frame(self.notebook)  # Creating a frame for the movies tab
        self.notebook.add(self.movie_tab, text="Movies")  # Adding the frame to the notebook with a label
        self.movie_text = scrolledtext.ScrolledText(self.movie_tab, wrap=tk.WORD, height=10, state='disabled')
        self.movie_text.pack(fill=tk.BOTH, expand=True)  # Packing the text area to fill the frame and expand with it
        self.movie_stats_text = scrolledtext.ScrolledText(self.movie_tab, wrap=tk.WORD, height=10, state='disabled')
        self.movie_stats_text.pack(fill=tk.BOTH, expand=True)  # Another text area for displaying movie statistics
        self.movie_text.insert(tk.END, "No movie data loaded yet.")  # Placeholder text
        self.movie_stats_text.insert(tk.END, "No movie statistics available yet.")  # Placeholder text

    def create_tv_show_tab(self):
        """
        Creates a tab specifically for TV show data and statistics.
        """
        self.tv_show_tab = ttk.Frame(self.notebook)  # Frame for TV shows
        self.notebook.add(self.tv_show_tab, text="TV Shows")  # Adding the frame to the notebook
        self.tv_show_text = scrolledtext.ScrolledText(self.tv_show_tab, wrap=tk.WORD, height=10, state='disabled')
        self.tv_show_text.pack(fill=tk.BOTH, expand=True)  # Text area for TV show data
        self.tv_show_stats_text = scrolledtext.ScrolledText(self.tv_show_tab, wrap=tk.WORD, height=10, state='disabled')
        self.tv_show_stats_text.pack(fill=tk.BOTH, expand=True)  # Text area for TV show statistics
        self.tv_show_text.insert(tk.END, "No TV show data loaded yet.")  # Placeholder text
        self.tv_show_stats_text.insert(tk.END, "No TV show statistics available yet.")  # Placeholder text

    def create_book_tab(self):
        """
        Creates a tab for displaying book data and statistics within the application.
        This tab contains text areas for displaying book data and statistical information.
        """
        self.book_tab = ttk.Frame(self.notebook)  # Creating a frame for the book tab
        self.notebook.add(self.book_tab, text="Books")  # Adding this frame to the notebook with a label
        self.book_text = scrolledtext.ScrolledText(self.book_tab, wrap=tk.WORD, height=10, state='disabled')  # Text area for book data
        self.book_text.pack(fill=tk.BOTH, expand=True)  # Packing to make it fill the space and expandable
        self.book_stats_text = scrolledtext.ScrolledText(self.book_tab, wrap=tk.WORD, height=10, state='disabled')  # Text area for book stats
        self.book_stats_text.pack(fill=tk.BOTH, expand=True)  # Packing to make it fill the space and expandable
        self.book_text.insert(tk.END, "No book data loaded yet.")  # Placeholder text
        self.book_stats_text.insert(tk.END, "No book statistics available yet.")  # Placeholder text

    def create_search_tab(self):
        """
        Creates a tab for searching through movies and TV shows.
        This tab includes multiple entries for different search criteria like type, title, director, etc.
        """
        self.search_tab = ttk.Frame(self.notebook)  # Creating a frame for the search tab
        self.notebook.add(self.search_tab, text="Search Movies/TV")  # Adding this frame to the notebook with a label

        # Defining frames for different search criteria and organize them vertically
        type_frame = ttk.Frame(self.search_tab)  # Frame for type selection
        title_frame = ttk.Frame(self.search_tab)  # Frame for title input
        director_frame = ttk.Frame(self.search_tab)  # Frame for director input
        actor_frame = ttk.Frame(self.search_tab)  # Frame for actor input
        genre_frame = ttk.Frame(self.search_tab)  # Frame for genre input
        search_button_frame = ttk.Frame(self.search_tab)  # Frame for search button

        # Packing all frames to fill horizontally
        type_frame.pack(fill='x')
        title_frame.pack(fill='x')
        director_frame.pack(fill='x')
        actor_frame.pack(fill='x')
        genre_frame.pack(fill='x')
        search_button_frame.pack(fill='x')

        # Creating and place UI elements within their respective frames
        ttk.Label(type_frame, text="Type:").pack(side='left', fill='x', pady=3)
        self.type_combobox = ttk.Combobox(type_frame, values=["Movie", "TV Show"], width=27)
        self.type_combobox.pack(side='left', padx=5)

        ttk.Label(title_frame, text="Title:").pack(side='left', fill='x', pady=3)
        self.title_entry = ttk.Entry(title_frame, width=50)
        self.title_entry.pack(side='left', padx=5)

        ttk.Label(director_frame, text="Director:").pack(side='left', fill='x', pady=3)
        self.director_entry = ttk.Entry(director_frame, width=50)
        self.director_entry.pack(side='left', padx=5)

        ttk.Label(actor_frame, text="Actor:").pack(side='left', fill='x', pady=3)
        self.actor_entry = ttk.Entry(actor_frame, width=50)
        self.actor_entry.pack(side='left', padx=5)

        ttk.Label(genre_frame, text="Genre:").pack(side='left', fill='x', pady=3)
        self.genre_entry = ttk.Entry(genre_frame, width=50)
        self.genre_entry.pack(side='left', padx=5)

        ttk.Button(search_button_frame, text="Search", command=self.searchShows).pack(side='left', ipadx=4, ipady=4, fill='x')

        # Text area for displaying search results
        self.search_text = scrolledtext.ScrolledText(self.search_tab, wrap=tk.WORD, height=10)
        self.search_text.pack(fill='both', expand=True)

    def create_search_books_tab(self):
        """Creates a tab for searching books."""
        self.search_books_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.search_books_tab, text="Search Books")

        # Creating frames for each row to ensure consistent alignment
        title_frame = ttk.Frame(self.search_books_tab)
        author_frame = ttk.Frame(self.search_books_tab)
        publisher_frame = ttk.Frame(self.search_books_tab)
        search_button_frame = ttk.Frame(self.search_books_tab)

        # Packing frames
        title_frame.pack(fill='x', padx=10, pady=3)
        author_frame.pack(fill='x', padx=10, pady=3)
        publisher_frame.pack(fill='x', padx=10, pady=3)
        search_button_frame.pack(fill='x', padx=10)

        # Title Entry
        ttk.Label(title_frame, text="Title:").pack(side='left')
        self.title_book_entry = ttk.Entry(title_frame, width=50)
        self.title_book_entry.pack(side='left', padx=5)

        # Author Entry
        ttk.Label(author_frame, text="Author:").pack(side='left')
        self.author_entry = ttk.Entry(author_frame, width=50)
        self.author_entry.pack(side='left', padx=5)

        # Publisher Entry
        ttk.Label(publisher_frame, text="Publisher:").pack(side='left')
        self.publisher_entry = ttk.Entry(publisher_frame, width=50)
        self.publisher_entry.pack(side='left', padx=5)

        # Search Button
        ttk.Button(search_button_frame, text="Search", command=self.searchBooks).pack(side='left', fill='x', ipadx=3)

        # Text area for results
        self.book_search_text = scrolledtext.ScrolledText(self.search_books_tab, wrap=tk.WORD, height=15)
        self.book_search_text.pack(fill='both', expand=True, padx=10, pady=10)

    def create_recommendation_tab(self):
        """Create a tab for getting recommendations."""
        self.recommendation_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.recommendation_tab, text="Recommendations")

        # Creating frames for each row
        type_frame = ttk.Frame(self.recommendation_tab)
        title_frame = ttk.Frame(self.recommendation_tab)
        button_frame = ttk.Frame(self.recommendation_tab)

        # Packing frames
        type_frame.pack(fill='x', padx=8, pady=1)
        title_frame.pack(fill='x', padx=6, pady=1)
        button_frame.pack(fill='x', padx=10)

        # Media Type ComboBox
        ttk.Label(type_frame, text="Type:").pack(side='left')
        self.rec_type_combobox = ttk.Combobox(type_frame, values=["Movie", "TV Show", "Book"], width=27)
        self.rec_type_combobox.pack(side='left', padx=5)

        # Title Entry
        ttk.Label(title_frame, text="Title:").pack(side='left')
        self.rec_title_entry = ttk.Entry(title_frame, width=50)
        self.rec_title_entry.pack(side='left', padx=5)

        # Recommendation Button
        ttk.Button(button_frame, text="Get Recommendation", command=self.getRecommendations).pack(side='left', fill='x',
                                                                                                  ipadx=10)

        # Text Area for Recommendations
        self.recommendation_text = scrolledtext.ScrolledText(self.recommendation_tab, wrap=tk.WORD, height=15)
        self.recommendation_text.pack(fill='both', expand=True, padx=10)

    def create_bottom_buttons(self):
        """Create bottom buttons for loading data and other functionalities."""
        # Setting uniform padding and side alignment
        button_padding = {'padx': 105, 'pady': 5, 'ipadx': 3, 'ipady': 3}

        # Creating buttons for different functionalities and packing them to the left side of the window
        ttk.Button(self.root, text="Load Shows", command=self.loadShows).pack(side=tk.LEFT, **button_padding)
        ttk.Button(self.root, text="Load Books", command=self.loadBooks).pack(side=tk.LEFT, **button_padding)
        ttk.Button(self.root, text="Load Recommendations", command=self.loadAssociations).pack(side=tk.LEFT,
                                                                                            **button_padding)
        ttk.Button(self.root, text="Information", command=self.creditInfoBox).pack(side=tk.LEFT, **button_padding)
        ttk.Button(self.root, text="Quit", command=self.root.quit).pack(side=tk.LEFT, **button_padding)

    def loadShows(self):
        """
        Load data for TV shows and movies from an external source and update the GUI to display the loaded data.
        This method updates various text areas dedicated to movies and TV shows with their respective data and statistics.
        """
        # Attempt to load shows from an external source
        self.recommender.loadShows()
        try:
            movie_text = '\n'.join(self.recommender.getMovieList())
            movie_stats = self.recommender.getMovieStats()
            tv_show_text = '\n'.join(self.recommender.getTVList())
            tv_show_stats = self.recommender.getTVStats()
        except:
            return
        self.movie_text.config(state='normal')
        self.movie_text.delete(1.0, tk.END)
        self.movie_text.insert(tk.END, movie_text)
        self.movie_text.config(state='disabled')
        self.movie_stats_text.config(state='normal')
        self.movie_stats_text.delete(1.0, tk.END)
        self.movie_stats_text.insert(tk.END, movie_stats)
        self.movie_stats_text.config(state='disabled')
        self.tv_show_text.config(state='normal')
        self.tv_show_text.delete(1.0, tk.END)
        self.tv_show_text.insert(tk.END, tv_show_text)
        self.tv_show_text.config(state='disabled')
        self.tv_show_stats_text.config(state='normal')
        self.tv_show_stats_text.delete(1.0, tk.END)
        self.tv_show_stats_text.insert(tk.END, tv_show_stats)
        self.tv_show_stats_text.config(state='disabled')

        # Updating the ratings charts if new data has been loaded
        self.update_ratings_charts()

    def loadBooks(self):
        """
        Loads book data from an external source and update the GUI to display the loaded book data and statistics.
        """
        # Load books using the recommender's method
        self.recommender.loadBooks()
        try:
            book_text = '\n'.join(self.recommender.getBookList())
            book_stats = self.recommender.getBookStats()
        except:
            return
        self.book_text.config(state='normal')
        self.book_text.delete(1.0, tk.END)
        self.book_text.insert(tk.END, book_text)
        self.book_text.config(state='disabled')
        self.book_stats_text.config(state='normal')
        self.book_stats_text.delete(1.0, tk.END)
        self.book_stats_text.insert(tk.END, book_stats)
        self.book_stats_text.config(state='disabled')

    def loadAssociations(self):
        """
        Loads associations data from an external file. This data typically includes links
        between different media types, such as shows and books.
        """
        self.recommender.loadAssociations()

    def creditInfoBox(self):
        """
        Display's credits information for the application.
        """
        messagebox.showinfo("credit", " 1. Karthik Samudrala\n 2. Baby Sahithi Samudrala\n 3. Jaswanth Kolisetty\n\n Developed on Date: May 5th, 2024")

    def searchShows(self):
        """
        Search for shows based on user input criteria including type, title, director,
        actor, and genre, then display the search results in the GUI.
        """
        media_type = self.type_combobox.get()
        title = self.title_entry.get()
        director = self.director_entry.get()
        actor = self.actor_entry.get()
        genre = self.genre_entry.get()
        results = self.recommender.searchTVMovies(media_type, title, director, actor, genre)
        self.search_text.config(state='normal')
        self.search_text.delete(1.0, tk.END)
        self.search_text.insert(tk.END, results)
        self.search_text.config(state='disabled')

    def searchBooks(self):
        """
        Searching for books based on user input criteria including title, author, and publisher,
        then display the search results in the GUI.
        """
        title = self.title_book_entry.get()
        author = self.author_entry.get()
        publisher = self.publisher_entry.get()
        results = self.recommender.searchBooks(title, author, publisher)
        self.book_search_text.config(state='normal')
        self.book_search_text.delete(1.0, tk.END)
        self.book_search_text.insert(tk.END, results)
        self.book_search_text.config(state='disabled')

    def getRecommendations(self):
        """
        Fetching and display recommendations based on the type and title specified by the user.
        This function handles both movies/TV shows and books.
        """
        media_type = self.rec_type_combobox.get()
        title = self.rec_title_entry.get()
        if not media_type or not title:
            messagebox.showerror("Error", "Please fill both Type and Title fields.")
            return
        results = self.recommender.getRecommendations(media_type, title)
        self.recommendation_text.config(state='normal')
        self.recommendation_text.delete(1.0, tk.END)
        self.recommendation_text.insert(tk.END, results)
        self.recommendation_text.config(state='disabled')


def main():
    """Main function to initialize the GUI."""
    gui = RecommenderGUI()
    gui.root.mainloop()


main()
