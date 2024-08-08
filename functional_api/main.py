from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
from Database import db_session, engine
import schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = db_session()  # Instantiate the session
    try:
        yield db
    finally:
        db.close()

# CRUD operations for Projects
@app.post("/projects/", response_model=schemas.Project)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    db_project = models.Project(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

@app.get("/projects/", response_model=list[schemas.Project])
def read_projects(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Project).offset(skip).limit(limit).all()

@app.get("/projects/{project_id}", response_model=schemas.Project)
def read_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@app.put("/projects/{project_id}", response_model=schemas.Project)
def update_project(project_id: int, project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    db_project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    db_project.title = project.title
    db_project.description = project.description
    db_project.url = project.url
    db.commit()
    db.refresh(db_project)
    return db_project

@app.delete("/projects/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db)):
    db_project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    db.delete(db_project)
    db.commit()
    return {"detail": "Project deleted"}

# CRUD operations for BlogPosts
@app.post("/blogposts/", response_model=schemas.BlogPost)
def create_blogpost(blogpost: schemas.BlogPostCreate, db: Session = Depends(get_db)):
    db_blogpost = models.BlogPost(**blogpost.dict())
    db.add(db_blogpost)
    db.commit()
    db.refresh(db_blogpost)
    return db_blogpost

@app.get("/blogposts/", response_model=list[schemas.BlogPost])
def read_blogposts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.BlogPost).offset(skip).limit(limit).all()

@app.get("/blogposts/{blogpost_id}", response_model=schemas.BlogPost)
def read_blogpost(blogpost_id: int, db: Session = Depends(get_db)):
    blogpost = db.query(models.BlogPost).filter(models.BlogPost.id == blogpost_id).first()
    if blogpost is None:
        raise HTTPException(status_code=404, detail="Blog post not found")
    return blogpost

@app.put("/blogposts/{blogpost_id}", response_model=schemas.BlogPost)
def update_blogpost(blogpost_id: int, blogpost: schemas.BlogPostCreate, db: Session = Depends(get_db)):
    db_blogpost = db.query(models.BlogPost).filter(models.BlogPost.id == blogpost_id).first()
    if db_blogpost is None:
        raise HTTPException(status_code=404, detail="Blog post not found")
    db_blogpost.title = blogpost.title
    db_blogpost.content = blogpost.content
    db_blogpost.url = blogpost.url
    db.commit()
    db.refresh(db_blogpost)
    return db_blogpost

@app.delete("/blogposts/{blogpost_id}")
def delete_blogpost(blogpost_id: int, db: Session = Depends(get_db)):
    db_blogpost = db.query(models.BlogPost).filter(models.BlogPost.id == blogpost_id).first()
    if db_blogpost is None:
        raise HTTPException(status_code=404, detail="Blog post not found")
    db.delete(db_blogpost)
    db.commit()
    return {"detail": "Blog post deleted"}

# CRUD operations for Contacts
@app.post("/contacts/", response_model=schemas.Contact)
def create_contact(contact: schemas.ContactCreate, db: Session = Depends(get_db)):
    db_contact = models.Contact(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

@app.put("/contacts/{contact_id}", response_model=schemas.Contact)
def update_contact(contact_id: int, contact: schemas.ContactCreate, db: Session = Depends(get_db)):
    db_contact = db.query(models.Contact).filter(models.Contact.id == contact_id).first()
    if db_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    db_contact.name = contact.name
    db_contact.email = contact.email
    db_contact.message = contact.message
    db.commit()
    db.refresh(db_contact)
    return db_contact

@app.delete("/contacts/{contact_id}")
def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    db_contact = db.query(models.Contact).filter(models.Contact.id == contact_id).first()
    if db_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    db.delete(db_contact)
    db.commit()
    return {"detail": "Contact deleted"}
