from src.models.Movies import Movies
class Node:
    def __init__(self,value: Movies):
        self.value = value
        self.left = None
        self.right = None
    def __repr__(self):
        return f"{self.value}"
    