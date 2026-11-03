from pydantic import BaseModel, Field


class Fruit(BaseModel):
    id: int = Field(ge=0)
    name: str
    price: float = Field(ge=0)
