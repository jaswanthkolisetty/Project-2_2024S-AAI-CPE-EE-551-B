import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from tkinter import filedialog
from Recommender import Recommender


class RecommenderGUI:
    def __init__(self):
        self.recommender = Recommender()

        # Create the main window
        self.root = tk.Tk()
        self.root.title("Media Recommender System")
        self.root.geometry("1200x800")

        # Create a Notebook
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both')

        # Add tabs
        self.create_movie_tab()
        self.create_tv_show_tab()
        self.create_book_tab()
        self.create_search_tab()
        self.create_recommendation_tab()

        # Bottom buttons
        self.create_bottom_buttons()



    def create_movie_tab(self):
        """Creates the tab for movies with statistics and list of movies."""
        self.movie_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.movie_tab, text="Movies")

        # Text areas for movie titles and statistics
        self.movie_text = scrolledtext.ScrolledText(self.movie_tab, wrap=tk.WORD, height=10, state='disabled')
        self.movie_text.pack(fill=tk.BOTH, expand=True)
        self.movie_stats_text = scrolledtext.ScrolledText(self.movie_tab, wrap=tk.WORD, height=10, state='disabled')
        self.movie_stats_text.pack(fill=tk.BOTH, expand=True)

        # Default text if no data loaded
        self.movie_text.insert(tk.END, "No movie data loaded yet.")
        self.movie_stats_text.insert(tk.END, "No movie statistics available yet.")

    def create_tv_show_tab(self):
        """Creates the tab for TV shows with statistics and list of TV shows."""
        self.tv_show_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.tv_show_tab, text="TV Shows")

        # Text areas
        self.tv_show_text = scrolledtext.ScrolledText(self.tv_show_tab, wrap=tk.WORD, height=10, state='disabled')
        self.tv_show_text.pack(fill=tk.BOTH, expand=True)
        self.tv_show_stats_text = scrolledtext.ScrolledText(self.tv_show_tab, wrap=tk.WORD, height=10, state='disabled')
        self.tv_show_stats_text.pack(fill=tk.BOTH, expand=True)

        self.tv_show_text.insert(tk.END, "No TV show data loaded yet.")
        self.tv_show_stats_text.insert(tk.END, "No TV show statistics available yet.")

    def create_book_tab(self):
        """Creates the tab for books with statistics and list of books."""
        self.book_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.book_tab, text="Books")

        # Text areas
        self.book_text = scrolledtext.ScrolledText(self.book_tab, wrap=tk.WORD, height=10, state='disabled')
        self.book_text.pack(fill=tk.BOTH, expand=True)
        self.book_stats_text = scrolledtext.ScrolledText(self.book_tab, wrap=tk.WORD, height=10, state='disabled')
        self.book_stats_text.pack(fill=tk.BOTH, expand=True)

        self.book_text.insert(tk.END, "No book data loaded yet.")
        self.book_stats_text.insert(tk.END, "No book statistics available yet.")

    def create_search_tab(self):
        """Creates the tab for searching through media."""
        self.search_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.search_tab, text="Search Media")
        # Include widgets for search functionality

    def create_recommendation_tab(self):
        """Creates the tab for getting recommendations."""
        self.recommendation_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.recommendation_tab, text="Recommendations")
        # Include widgets for recommendation functionality

    def create_bottom_buttons(self):
        """Creates buttons for loading data and other utilities."""
        ttk.Button(self.root, text="Load Shows", command=self.loadShows).pack(side=tk.LEFT)
        ttk.Button(self.root, text="Load Books", command=self.loadBooks).pack(side=tk.LEFT)
        ttk.Button(self.root, text="Load Associations", command=self.loadAssociations).pack(side=tk.LEFT)
        ttk.Button(self.root, text="Credits", command=self.creditInfoBox).pack(side=tk.LEFT)
        ttk.Button(self.root, text="Quit", command=self.root.quit).pack(side=tk.RIGHT)

    def creditInfoBox(self):
        """Displays credit information."""
        messagebox.showinfo("Credits", "Developed by Team XYZ")

    def loadShows(self):
        self.recommender.loadShows()  # Load show data
        movie_text = self.recommender.getMovieList()  # Get movie list and stats
        movie_stats = self.recommender.getMovieStats()
        tv_show_text = self.recommender.getTVList()  # Get TV show list and stats
        tv_show_stats = self.recommender.getTVStats()

        # Update the text areas for movies
        self.movie_text.config(state='normal')
        self.movie_text.delete(1.0, tk.END)
        self.movie_text.insert(tk.END, movie_text)
        self.movie_text.config(state='disabled')

        self.movie_stats_text.config(state='normal')
        self.movie_stats_text.delete(1.0, tk.END)
        self.movie_stats_text.insert(tk.END, movie_stats)
        self.movie_stats_text.config(state='disabled')

        # Update the text areas for TV shows
        self.tv_show_text.config(state='normal')
        self.tv_show_text.delete(1.0, tk.END)
        self.tv_show_text.insert(tk.END, tv_show_text)
        self.tv_show_text.config(state='disabled')

        self.tv_show_stats_text.config(state='normal')
        self.tv_show_stats_text.delete(1.0, tk.END)
        self.tv_show_stats_text.insert(tk.END, tv_show_stats)
        self.tv_show_stats_text.config(state='disabled')

    def loadBooks(self):
        self.recommender.loadBooks()
        print(self.recommender.loadBooks())  # Load book data
        book_text = self.recommender.getBookList()  # Get book list and stats
        print(book_text)
        book_stats = self.recommender.getBookStats()

        # Update the text area for books
        self.book_text.config(state='normal')
        self.book_text.delete(1.0, tk.END)
        self.book_text.insert(tk.END, book_text)
        self.book_text.config(state='disabled')

        self.book_stats_text.config(state='normal')
        self.book_stats_text.delete(1.0, tk.END)
        self.book_stats_text.insert(tk.END, book_stats)
        self.book_stats_text.config(state='disabled')

    def loadAssociations(self):
        self.recommender.loadAssociations()  # Load association data

    def creditInfoBox(self):
        messagebox.showinfo("Credits", "Project completed by:\n- Alice\n- Bob\n- Charlie\nCompleted on: 2024-05-01")

    def searchShows(self):
        # Extract data from GUI
        media_type = self.type_combobox.get()  # Assuming a ttk.Combobox exists
        title = self.title_entry.get()  # Assuming a ttk.Entry exists
        director = self.director_entry.get()
        actor = self.actor_entry.get()
        genre = self.genre_entry.get()

        results = self.recommender.searchShows(media_type, title, director, actor, genre)
        self.search_text.config(state='normal')
        self.search_text.delete(1.0, tk.END)
        self.search_text.insert(tk.END, results)
        self.search_text.config(state='disabled')

    def searchBooks(self):
        title = self.title_book_entry.get()
        author = self.author_entry.get()
        publisher = self.publisher_entry.get()

        results = self.recommender.searchBooks(title, author, publisher)
        self.book_search_text.config(state='normal')
        self.book_search_text.delete(1.0, tk.END)
        self.book_search_text.insert(tk.END, results)
        self.book_search_text.config(state='disabled')

    def getRecommendations(self):
        media_type = self.rec_type_combobox.get()  # Assuming a ttk.Combobox exists
        title = self.rec_title_entry.get()  # Assuming a ttk.Entry exists

        results = self.recommender.getRecommendations(media_type, title)
        self.recommendation_text.config(state='normal')
        self.recommendation_text.delete(1.0, tk.END)
        self.recommendation_text.insert(tk.END, results)
        self.recommendation_text.config(state='disabled')

def main():
    gui = RecommenderGUI()
    gui.root.mainloop()

main()
