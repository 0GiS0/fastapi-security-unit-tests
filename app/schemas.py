from datetime import datetime
from typing import List
from pydantic import BaseModel, validator


class UserBaseSchema(BaseModel):
    id: str | None = None
    first_name: str
    last_name: str
    email: str
    username: str
    password: str
    address: str | None = None
    activated: bool = False
    createdAt: datetime | None = None
    updatedAt: datetime | None = None

    @validator("username")
    def username_is_not_common(cls, v):
        if v in ["admin", "root", "superuser", "guest", "adm", "user"]: #https://github.com/danielmiessler/SecLists/blob/master/Usernames/top-usernames-shortlist.txt
            raise ValueError("Username cannot be admin")
        return v

    @validator("email")
    def email_must_contain_at(cls, v):
        if "@" not in v:
            raise ValueError("Email must contain an @ symbol")
        return v

    @validator("password")
    def password_length_and_is_not_common(cls, v):
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters")
        return v

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class ListUserResponse(BaseModel):
    status: str
    results: int
    users: List[UserBaseSchema]
