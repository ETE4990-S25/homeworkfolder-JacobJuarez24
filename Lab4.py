import json

# Load data from JSON file
def load_dataset(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return "The file could not be found"
    except json.JSONDecodeError:
        return "The file could not be decoded"
    
#Function for user to pick movie 
def pick_movie(data, min_rating, max year):
    if isinstance(data, str):
        return data #return the error message if loadin data failed
        
    filter_movies = []

    #Filter movies by year and rating
    for movie in data:
        if movie.get('Rating') >= min_rating and movie.get('Year') <= max_year:
            filtered_movies.append(movie)
    
    if not filtered_movies:
        return "No movie match your search"
        
    #Return the first movie to filtered list
    return filtered_movies[0]
    
# Main User interface
def main():
    
    data = load_dataset("movies.json")

    #Movie selection
    min_rating = float(input("Enter the lowest rating to you would like to see (1-10): "))
    max_year = int(input("Enter the most recent release date you'd like to see: "))
    
    selected_movie = pick_movie(data, min_rating, max_year)
    
    #Display details
    if isinstance(selected_movie, str):
        print(selected_movie) #display error 
    else:
        print(f"Selected_Movie:{selected_movie['Title']}")
        print(f"Year: {selected_movie['Year']}")
        print(f"Rating: {selected_movie['Rating']}")

#Run main function
if __name__ == "__main__":
    main()
