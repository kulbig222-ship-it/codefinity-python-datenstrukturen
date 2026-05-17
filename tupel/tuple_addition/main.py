animal_movies = ('The Lion King', 'Jurassic Park', 'Finding Nemo')

# Write your code here
animal_movies_list = list(animal_movies)
animal_movies_list.append("Dumbo")
animal_movies_list.append("Zootopia")
animal_movies = tuple(animal_movies_list)
del animal_movies_list

print("Updated animal movies:", animal_movies)