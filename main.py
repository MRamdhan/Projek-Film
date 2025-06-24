from data_loader import load_data
from recommender import get_recommendations
from visual import plot_genre_distribution, plot_avg_rating

if __name__ == '__main__':
    data = load_data('data/film.csv')
    if not data:
        exit(1)

    print("============================")
    print("  SISTEM REKOMENDASI FILM  ")
    print("============================")

    # Tambahan fitur genre tersedia
    available_genres = sorted(set(film['genre'].title() for film in data))
    print("\nGenre tersedia:", ", ".join(available_genres))

    genre = input("Masukkan genre favorit: ")
    
    try:
        min_rating = float(input("Masukkan rating minimal: "))
    except ValueError:
        print("Rating harus berupa angka.")
        exit(1)

    print("\nRekomendasi Film:")
    rekomendasi = get_recommendations(data, genre, min_rating)
    if rekomendasi:
        for idx, film in enumerate(rekomendasi, start=1):
            print(f"{idx}. {film['judul']} ({film['tahun']}) - Rating: {film['rating']}")
    else:
        print("Tidak ada film yang sesuai.")

    plot_genre_distribution(data)
    plot_avg_rating(data)
    print("\nGrafik disimpan di folder 'img'")
