def get_recommendations(data, genre, min_rating):
    filtered = [
        film for film in data 
        if film['genre'].lower() == genre.lower() and film['rating'] >= min_rating
    ]
    return sorted(filtered, key=lambda x: x['rating'], reverse=True)
