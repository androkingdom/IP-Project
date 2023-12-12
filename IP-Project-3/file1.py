import mysql.connector as sqLtor
import pandas as pd
import matplotlib.pyplot as plt

# Database connection details
host = "localhost"
user = "root"
password = "1234"
database = "movie"

# Connect to MySQL database
db_connection = sqLtor.connect(host=host,user=user,password=password,database=database)
cursor = dbconnection.cursor()

# Function to fetch movie data
def get_movies():
  cursor.execute("SELECT id, title, year FROM movies")
  data = cursor.fetchall()
  movies = pd.DataFrame(data, columns=["id", "title", "year"])
  return movies

# Function to fetch movie ratings
def get_ratings(movie_id):
  cursor.execute("SELECT rating FROM ratings WHERE movie_id=%s", (movie_id,))
  data = cursor.fetchall()
  ratings = pd.DataFrame(data, columns=["rating"])
  return ratings

# Main function
def main():
  # Get all movies
  movies = get_movies()

  # User input for movie selection
  movie_id = int(input("Enter movie ID: "))

  # Get movie ratings for selected movie
  ratings = get_ratings(movie_id)

  # Calculate statistics
  average_rating = ratings["rating"].mean()
  rating_distribution = ratings["rating"].value_counts()

  # Generate charts
  plt.figure(figsize=(8, 6))
  plt.bar(rating_distribution.index, rating_distribution.values)
  plt.xlabel("Rating")
  plt.ylabel("Number of Ratings")
  plt.title(f"Rating Distribution for Movie ID {movie_id}")
  plt.show()

  print(f"Average Rating: {average_rating:.2f}")

if __name__ == "__main__":
  main()