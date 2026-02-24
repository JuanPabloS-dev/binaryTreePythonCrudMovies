from src.node import Node
from src.tree import Tree
from src.api.api import get_api
from src.models.Movies import Movies
from helpers.balanced_insert import list_to_tree

data = get_api('https://devsapihub.com/api-movies')
balanced_data = list_to_tree(data)
arbol= Tree()

def insert(data:list):
    for d in data:
        movie = Movies(
            sku = d["id"],  
            name = d["title"], 
            year = d["year"],
            rating = d["stars"],
            description = d["description"],
            genres = d["genre"],
            poster = d["image_url"]
        )
        arbol.insert(Node(movie))

insert(balanced_data)
arbol.guardar_json()
