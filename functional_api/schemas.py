from pydantic import BaseModel

class ProjectBase(BaseModel):
    title: str
    description: str
    url: str

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int

    class Config:
        orm_mode = True

class BlogPostBase(BaseModel):
    title: str
    content: str
    url: str

class BlogPostCreate(BlogPostBase):
    pass

class BlogPost(BlogPostBase):
    id: int

    class Config:
        orm_mode = True

class ContactBase(BaseModel):
    name: str
    email: str
    message: str

class ContactCreate(ContactBase):
    pass

class Contact(ContactBase):
    id: int

    class Config:
        orm_mode = True
