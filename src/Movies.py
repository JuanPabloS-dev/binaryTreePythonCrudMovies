from typing import Optional,List
from uuid import uuid4
class Movies:
    def __init__(self,name: str, country: str , year: int,director:str,description:Optional[str],actors:List[str],poster:str ):
        self.id = uuid4()
        self.name = name
        self.country = country 
        self.year = year 
        self.director = director
        self.description = description
        self.actors = actors
        self.poster = poster 
