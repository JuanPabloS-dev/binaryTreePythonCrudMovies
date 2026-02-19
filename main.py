from src.node import Node
from src.tree import Tree

peliculas = Tree()
movies = peliculas.importar_json("movies.json")
for i in movies:
    movie = Node(i)
    peliculas.insertar(movie)
    
print(peliculas.size)
print(peliculas.buscar("Gladiator"))
for i in peliculas.recorrer("in"):
    print(i.value)

peliculas.guardar_json()


print(peliculas.eliminar("Gladiator"))
print(peliculas.eliminar("Parasite"))
print(peliculas.eliminar("Inception"))
print("-" * 40)
for i in peliculas.recorrer("in"):
    print(i.value)