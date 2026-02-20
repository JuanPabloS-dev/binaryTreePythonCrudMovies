import pytest
from src.Movies import Movies
from src.tree import Tree
from src.node import Node


@pytest.fixture
def pelicula_ejemplo():
    movie = Movies(
        name="Forrest Gump",
        country="Estados Unidos",
        year=1994,
        director="Robert Zemeckis",
        description="Historia de Forrest.",
        actors=["Tom Hanks"],
        poster="url"
    )
    return Node({
        "name": movie.name,
        "year": movie.year
    })


@pytest.fixture
def arbol():
    return Tree()


@pytest.fixture
def arbol_poblado():
    tree = Tree()

    nombres = ["M", "A", "Z", "B", "Y"]

    for n in nombres:
        tree.insertar(Node({"name": n}))

    return tree
