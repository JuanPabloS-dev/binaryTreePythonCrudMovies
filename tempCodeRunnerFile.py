peliculas = Tree()
for i in movies:
    movie = Node(i)
    peliculas.insertar(movie)
    
print(peliculas.size)