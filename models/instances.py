from pydantic import BaseModel
from typing import Optional


class CreateUser(BaseModel):
    username: str
    email: str
    password: str
    first_name :str
    last_name :str
    photo :str
    address :str
    cart_id : int
    role : str
    favorites : str

class CreateProduct(BaseModel):
    title: str
    photo: str
    price: float
    description: str
    amount: int
    category: str
    tags: str


class UpdateProduct(BaseModel):
    title: Optional[str] = None
    photo: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None
    amount: Optional[int] = None
    category: Optional[str] = None
    tags: Optional[str] = None
