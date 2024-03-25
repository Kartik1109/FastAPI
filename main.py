from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

from api import users, courses, sections  # Importing routers from separate files

app = FastAPI(
    title="Fast API LMS",  # Title of the API
    description="LMS for managing students and courses.",  # Description of what the API does
    version="0.0.1",  # Version of the API
    contact={
        "name": "Kartik",  # Contact person's name
        "email": "kartik@example.com",  # Contact person's email
    },
    license_info={
        "name": "MIT",  # License information for the API
    },
)

app.include_router(users.router)  # Include the users router
app.include_router(courses.router)  # Include the courses router
app.include_router(sections.router)  # Include the sections router
