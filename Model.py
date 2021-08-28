from pydantic import BaseModel
from datetime import datetime

#class Square(BaseModel):
    # square_id: int
    # lon: str  # долгота
    # lat: str  # широта
    # center_location_lon: str
    # center_location_lat: str


class Analys_data(BaseModel):
    request_id: int
    square_id: int
    date: datetime
    index_1: float
    index_2: float
    index_3: float
    index_4: float
    index_5: float
    index_6: float