from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .routers import post, user, auth, vote
from . import settings


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Social Media Application", description="""
    A social media app where users can sign up, create and manage posts, search and filter content, and vote on posts. It supports user authentication, real-time updates, and is built for security and scalability.
    """, version="0.1")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Welcome to social media application"}
