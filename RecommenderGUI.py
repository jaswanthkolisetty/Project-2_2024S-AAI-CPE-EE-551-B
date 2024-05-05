import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from tkinter import filedialog
from Recommender import Recommender

class RecommenderGUI:
    def __init__(self):
        self.recommender = Recommender()

        self.root = tk.Tk()
        self.root.title("Media Recommender System")
        self.root.geometry("1200x800")

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both')

        self.create_movie_tab()
        self.create_tv_show_tab()
        self.create_book_tab()
        self.create_search_tab()
        self.create_recommendation_tab()

        self.create_bottom_buttons()

    def create_movie_tab(self):
        self.movie_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.movie_tab, text="Movies")
        self.movie_text = scrolledtext.ScrolledText(self.movie_tab, wrap=tk.WORD, height=10, state='disabled')
        self.movie_text.pack(fill=tk.BOTH, expand=True)
        self.movie_stats_text = scrolledtext.ScrolledText(self.movie_tab, wrap=tk.WORD, height=10, state='disabled')
        self.movie_stats_text.pack(fill=tk.BOTH, expand=True)

    def create_tv_show_tab(self):
        self.tv_show_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.tv_show_tab, text="TV Shows")
        self.tv_show_text = scrolledtext.ScrolledText(self.tv_show_tab, wrap=tk.WORD, height=10, state='disabled')
        self.tv_show_text.pack(fill=tk.BOTH, expand=True)
        self.tv_show_stats_text = scrolledtext.ScrolledText(self.tv_show_tab, wrap=tk.WORD, height=10, state='disabled')
        self.tv_show_stats_text.pack(fill=tk.BOTH, expand=True)

    def create_book_tab(self):
        self.book_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.book_tab, text="Books")
        self.book_text = scrolledtext.ScrolledText(self.book_tab, wrap=tk.WORD, height=10, state='disabled')
        self.book_text.pack(fill=tk.BOTH, expand=True)
        self.book_stats_text = scrolledtext.ScrolledText(self.book_tab, wrap=tk.WORD, height=10, state='disabled')
        self.book_stats_text.pack(fill=tk.BOTH, expand=True)

    def create_search_tab(self):
        self.search_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.search_tab, text="Search Movies/TV")
        ttk.Label(self.search_tab, text="Type:").grid(row=0, column=0, padx=10, pady=10)
        self.type_combobox = ttk.Combobox(self.search_tab, values=["Movie", "TV Show"], width=17)
        self.type_combobox.grid(row=0, column=1, padx=10, pady=10)
        ttk.Label(self.search_tab, text="Title:").grid(row=1, column=0, padx=10, pady=10)
        self.title_entry = ttk.Entry(self.search_tab, width=20)
        self.title_entry.grid(row=1, column=1, padx=10, pady=10)
        ttk.Label(self.search_tab, text="Director:").grid(row=2, column=0, padx=10, pady=10)
        self.director_entry = ttk.Entry(self.search_tab, width=20)
        self.director_entry.grid(row=2, column=1, padx=10, pady=10)
        ttk.Label(self.search_tab, text="Actor:").grid(row=3, column=0, padx=10, pady=10)
        self.actor_entry = ttk.Entry(self.search_tab, width=20)
        self.actor_entry.grid(row=3, column=1, padx=10, pady=10)
        ttk.Label(self.search_tab, text="Genre:").grid(row=4, column=0, padx=10, pady=10)
        self.genre_entry = ttk.Entry(self.search_tab, width=20)
        self.genre_entry.grid(row=4, column=1, padx=10, pady=10)
        ttk.Button(self.search_tab, text="Search", command=self.searchShows).grid(row=5, column=0, columnspan=2, pady=10)
        self.search_text = scrolledtext.ScrolledText(self.search_tab, wrap=tk.WORD, height=15)
        self.search_text.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    def create_recommendation_tab(self):
        self.recommendation_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.recommendation_tab, text="Recommendations")

    def create_bottom_buttons(self):
        ttk.Button(self.root, text="Load Shows", command=self.loadShows).pack(side=tk.LEFT)
        ttk.Button(self.root, text="Load Books", command=self.loadBooks).pack(side=tk.LEFT)
        ttk.Button(self.root, text="Load Associations", command=self.loadAssociations).pack(side=tk.LEFT)
        ttk.Button(self.root, text="Credits", command=self.creditInfoBox).pack(side=tk.LEFT)
        ttk.Button(self.root, text="Quit", command=self.root.quit).pack(side=tk.RIGHT)

    def creditInfoBox(self):
        credit_info = "Project completed by:\n"
        credit_info += "- Karthik\n- Jaswanth\n- Sahithi\n"
        credit_info += "Completed on: 2024-05-01"
        messagebox.showinfo("Credits", credit_info)

    def loadShows(self):
        self.recommender.loadShows()
        movie_text = '\n'.join(self.recommender.getMovieList())
        movie_stats = '\n'.join([f"{key}: {value}" for key, value in self.recommender.getMovieStats().items()])
        tv_show_text = '\n'.join(self.recommender.getTVList())
        tv_show_stats = '\n'.join([f"{key}: {value}" for key, value in self.recommender.getTVStats().items()])
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

    def loadBooks(self):
        self.recommender.loadBooks()
        book_text = '\n'.join(self.recommender.getBookList())
        book_stats = '\n'.join([f"{key}: {value}" for key, value in self.recommender.getBookStats().items()])
        self.book_text.config(state='normal')
        self.book_text.delete(1.0, tk.END)
        self.book_text.insert(tk.END, book_text)
        self.book_text.config(state='disabled')
        self.book_stats_text.config(state='normal')
        self.book_stats_text.delete(1.0, tk.END)
        self.book_stats_text.insert(tk.END, book_stats)
        self.book_stats_text.config(state='disabled')

    def loadAssociations(self):
        self.recommender.loadAssociations()

    def searchShows(self):
        media_type = self.type_combobox.get()
        title = self.title_entry.get()
        director = self.director_entry.get()
        actor = self.actor_entry.get()
        genre = self.genre_entry.get()
        if media_type and (title or director or actor or genre):
            results = self.recommender.searchTVMovies(media_type, title, director, actor, genre)
            self.search_text.config(state='normal')
            self.search_text.delete(1.0, tk.END)
            self.search_text.insert(tk.END, results)
            self.search_text.config(state='disabled')
        else:
            messagebox.showerror("Error", "Please select 'Movie' or 'TV Show' and enter information for at least one field.")

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
        media_type = self.rec_type_combobox.get()
        title = self.rec_title_entry.get()
        results = self.recommender.getRecommendations(media_type, title)
        self.recommendation_text.config(state='normal')
        self.recommendation_text.delete(1.0, tk.END)
        self.recommendation_text.insert(tk.END, results)
        self.recommendation_text.config(state='disabled')

def main():
    gui = RecommenderGUI()
    gui.root.mainloop()

if __name__ == "__main__":
    main()




