from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID

class User(BaseModel):
    name: str
    email: EmailStr
    id: Optional[UUID] = None  # Changed to 'id' for consistency with common practices
    cv: Optional[bytes] = None  # Assuming 'cv' is a binary file, represented as bytes.