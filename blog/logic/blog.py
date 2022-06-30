from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(db, blog):
    new_blog = models.Blog(title=blog.title, body=blog.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def delete(id, db):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog {id} is not existing")
    blog.delete(synchronize_session=False)
    db.commit()


def update(id, db, request):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog {id} is not existing")
    blog.update(request.dict())
    db.commit()
    return 'updated'


def get(id, db):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog {id} is not existing")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f"Blog {id} is not existing"}
    return blog