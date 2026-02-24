from typing import Generator
from src.models.Movies import Movies
def list_to_tree(data: list) -> Generator[Movies,None,None]:
    if not data:
        return
    half = len(data)//2
    yield data[half]
    yield from list_to_tree(data[:half])
    yield from list_to_tree(data[half+1:])