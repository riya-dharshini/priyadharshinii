movies = {
    '1': 'Avengers: Endgame',
    '2': 'The Dark Knight',
    '3': 'Inception'
}

# Assume we have a database with available dates for each movie
# For simplicity, let's create a dictionary for available dates
movie_dates = {
    '1': ['2024-07-01', '2024-07-02', '2024-07-03'],
    '2': ['2024-07-01', '2024-07-02', '2024-07-03'],
    '3': ['2024-07-01', '2024-07-02', '2024-07-03']
}

def display_movies():
    print("Available Movies:")
    for key, value in movies.items():
        print(f"{key}. {value}")

def book_ticket(movie_id, date):
    movie_name = movies.get(movie_id)
    if movie_name:
        if date in movie_dates.get(movie_id, []):
    
            print(f"Ticket booked for {movie_name} on {date}")
        else:
            print("Invalid date. Please choose from available dates.")
    else:
        print("Invalid movie selection.")

display_movies()
choice = input("Enter movie ID to book ticket: ")
if choice in movies:
    selected_movie_id = choice
    print(f"Available dates for {movies[selected_movie_id]}:")
    print(movie_dates[selected_movie_id])
    selected_date = input("Enter date to book ticket (YYYY-MM-DD): ")
    book_ticket(selected_movie_id, selected_date)
else:
    print("Invalid movie selection.")

