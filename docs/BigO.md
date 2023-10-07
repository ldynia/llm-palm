﻿# GitHub Copilot Chat

Calculate the algorithm complexity of recommend method. Comment every line with Big O notation.


# ChatGPT-4

Calculate the algorithm complexity of recommend method. Comment every line with Big O notation.



# PaLM

You are Python expert and a computer scientist.

Calculate code complexity of recommended method using Big O notation.

Walk through code and comment every line with Big O notation.

```python
import random


class Sherlock():
    """
    Movies recommendation engine.
    """

    def __init__(self, movies, features):
        self.movies = movies
        self.title = features.get("title")
        self.features = ["genre", "stars"]

    def recommend(self):
        """
        Algorithm recommends movies based on default movie features.
        The algorithm uses partial match as search criteria and returns sorted list of movie(s).
        """
        ref_movie = self.__get_movie(self.title)
        if not ref_movie:
            return self.__lucky_recommendation(self.movies)
        ref_movie = ref_movie[0]

        movies = []
        for movie in self.movies:
            if movie["title"] != self.title:
                for feature in self.features:
                    feature_match = [fm in movie[feature] for fm in ref_movie[feature]]
                    if any(feature_match):
                        movies.append(movie)
                        break

        return sorted(movies, key=lambda movie: movie["rating"], reverse=True)


    def __lucky_recommendation(self, movies):
        """
        I feel lucky - random choice.
        """
        return [random.choice(movies)]

    def __get_movie(self, title):
        """
        Find movie by title.
        """
        movie = [movie for movie in self.movies if movie["title"] == title]
        return movie if movie else []
```