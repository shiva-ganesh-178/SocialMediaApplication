from pydantic import BaseModel, EmailStr, validator, Field
from datetime import datetime
from typing import Optional
from enum import Enum




class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True


class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length = 8)
    
    @validator('password')
    def password_must_contain_uppercase_and_number(cls, value):
        if not re.search(r'[A-Z]', value):
            raise ValueError('password must contain at least one uppercase letter')
        if not re.search(r'[0-9]', value):
            raise ValueError('password must contain at least one number')
        return value


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    # id: Optional[str] = None
    id: str


class VoteDir(int, Enum):
    one="1"
    zero="0"


class Vote(BaseModel):
    post_id: int
    # dir: conint(le=1)
    dir: VoteDir
