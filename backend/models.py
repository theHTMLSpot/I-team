from pydantic import BaseModel, EmailStr, root_validator
from typing import Optional, Union
from uuid import UUID

class User(BaseModel):
    name: str
    email: EmailStr
    id: Optional[UUID] = None  # Changed to 'id' for consistency with common practices
    verified: bool = False
    admin: bool = False
    description: Optional[str] = None
    cv: Optional[str] = None

    @root_validator(pre=True)
    def check_fields(cls, values):
        verified = values.get('verified', False)
        if verified:
            values['cv'] = None
        else:
            values['description'] = None
        return values