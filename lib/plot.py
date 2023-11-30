import matplotlib.pyplot as plt

def plot_genre_hist(data, title, x_label="Genre", y_label="Count"):
    plt.hist(data)
    plt.title(title)
    plt.xlabel("Genre")
    plt.ylabel("Count")
    plt.xticks(rotation=70)
    plt.show()
