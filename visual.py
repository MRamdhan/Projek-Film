import matplotlib.pyplot as plt
from collections import defaultdict

def plot_genre_distribution(data):
    genre_count = defaultdict(int)
    for film in data:
        genre_count[film['genre']] += 1

    plt.figure(figsize=(6,6))
    plt.pie(genre_count.values(), labels=genre_count.keys(), autopct='%1.1f%%')
    plt.title("Jumlah Film per Genre")
    plt.savefig("img/genre_pie.png")
    plt.close()

def plot_avg_rating(data):
    rating_sum = defaultdict(float)
    count = defaultdict(int)

    for film in data:
        genre = film['genre']
        rating_sum[genre] += film['rating']
        count[genre] += 1

    avg_rating = {g: rating_sum[g]/count[g] for g in rating_sum}

    plt.figure(figsize=(8,5))
    plt.bar(avg_rating.keys(), avg_rating.values(), color='skyblue')
    plt.title("Rata-rata Rating per Genre")
    plt.ylabel("Rating")
    plt.savefig("img/genre_rating_bar.png")
    plt.close()
