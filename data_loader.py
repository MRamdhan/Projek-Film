import csv

def load_data(filepath):
    try:
        with open(filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            return [
                {
                    'judul': row['Judul'],
                    'genre': row['genre'],
                    'rating': float(row['rating']),
                    'tahun': int(row['tahun'])
                } for row in reader
            ]
    except FileNotFoundError:
        print("File tidak ditemukan.")
        return []
