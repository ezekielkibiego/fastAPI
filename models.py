from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID, uuid4
from enum import Enum


class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"
    staff = "staff"

class User (BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    middle_name: Optional[str]
    last_name: str
    gender: Gender
    roles: List[Role]

    
