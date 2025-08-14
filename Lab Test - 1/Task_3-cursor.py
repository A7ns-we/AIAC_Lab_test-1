def recommend_movies(preferred_genre):
    """
    Recommend movies based on user's preferred genre.
    
    Args:
        preferred_genre (str): The genre the user likes
    
    Returns:
        list: List of movies matching the preferred genre
    """
    
    # Movie database with movies and their genres
    movies = [
        {"title": "Batman", "genre": "fiction"},
        {"title": "Inception", "genre": "thriller"},
        {"title": "Spider-Man", "genre": "action"},
        {"title": "The Dark Knight", "genre": "thriller"},
        {"title": "Iron Man", "genre": "action"},
        {"title": "Superman", "genre": "fiction"},
        {"title": "Mission Impossible", "genre": "action"},
        {"title": "The Matrix", "genre": "fiction"},
        {"title": "John Wick", "genre": "action"},
        {"title": "Interstellar", "genre": "fiction"},
        {"title": "The Silence of the Lambs", "genre": "thriller"},
        {"title": "Fight Club", "genre": "thriller"},
        {"title": "Avengers", "genre": "action"},
        {"title": "Black Panther", "genre": "action"},
        {"title": "Wonder Woman", "genre": "action"},
        {"title": "The Shawshank Redemption", "genre": "drama"},
        {"title": "Forrest Gump", "genre": "drama"},
        {"title": "Titanic", "genre": "romance"},
        {"title": "The Notebook", "genre": "romance"},
        {"title": "The Lion King", "genre": "animation"},
        {"title": "Toy Story", "genre": "animation"},
        {"title": "Frozen", "genre": "animation"},
        {"title": "The Exorcist", "genre": "horror"},
        {"title": "Halloween", "genre": "horror"},
        {"title": "A Nightmare on Elm Street", "genre": "horror"}
    ]
    
    # Find movies matching the preferred genre
    recommended_movies = []
    for movie in movies:
        if movie["genre"].lower() == preferred_genre.lower():
            recommended_movies.append(movie["title"])
    
    return recommended_movies


def main():
    """Main function to run the movie recommendation program."""
    
    print("🎬 Movie Recommendation System")
    print("=" * 40)
    
    # Show available genres
    available_genres = ["action", "thriller", "fiction", "drama", "romance", "animation", "horror"]
    
    print("\nAvailable genres:")
    for i, genre in enumerate(available_genres, 1):
        print(f"{i}. {genre}")
    
    # Get user input
    print("\nEnter your preferred genre:")
    user_genre = input("> ").strip()
    
    if not user_genre:
        print("No genre entered. Please try again.")
        return
    
    # Get recommendations
    recommendations = recommend_movies(user_genre)
    
    # Display results
    if recommendations:
        print(f"\n🎯 Movies recommended for '{user_genre}':")
        print("-" * 40)
        for i, movie in enumerate(recommendations, 1):
            print(f"{i}. {movie}")
    else:
        print(f"\n❌ No movies found for genre '{user_genre}'")
        print("Available genres:", ", ".join(available_genres))


# Run the program
if __name__ == "__main__":
    main()
