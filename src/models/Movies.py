from typing import Optional, List
from uuid import uuid4

class Movies:
    def __init__(
        self,
        sku: Optional[int] = None,
        name: str = "",
        year: int = 0,
        rating: float = 0.0,
        director: Optional[str] = None,
        genres: Optional[List[str]] = None,
        actors: Optional[List[str]] = None,
        poster: Optional[str] = None,
        description: Optional[str] = None
    ):
        self.id = uuid4()
        self.sku = sku
        self.name = name
        self.year = year
        self.rating = rating
        self.director = director
        self.genres = genres or []
        self.actors = actors or []
        self.poster = poster
        self.description = description
        
    def to_dict(self):
        return {
            "id": str(self.id),  # UUID necesita str
            "sku": self.sku,
            "name": self.name,
            "year": self.year,
            "rating": self.rating,
            "director": self.director,
            "genres": self.genres,
            "actors": self.actors,
            "poster": self.poster,
            "description": self.description
        }