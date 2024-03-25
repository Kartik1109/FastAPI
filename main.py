from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI(
    title="Fast API LMS",  # Title of the API
    description="LMS for managing students and courses.",  # Description of what the API does
    version="0.0.1",  # Version of the API
    contact={
        "name": "Gwen",  # Contact person's name
        "email": "gwen@example.com",  # Contact person's email
    },
    license_info={
        "name": "MIT",  # License information for the API
    },
)

users = []  # List to store user data

class User(BaseModel):
    email: str  # Email of the user, required
    is_active: bool  # Indicator of user's active status, required
    bio: Optional[str]  # Optional user biography

@app.get("/users", response_model=List[User])  # HTTP GET endpoint to fetch users
async def get_users():
    return users  # Return list of users

@app.post("/users")  # HTTP POST endpoint to create a new user
async def create_user(user: User):
    users.append(user)  # Add the new user to the list
    return "Success"  # Return success message

@app.get("/users/{id}")  # HTTP GET endpoint to fetch user by ID
async def get_user(
    id: int = Path(..., description="The ID of the user you want to retrieve.", gt=2),  # Path parameter for user ID
    q: str = Query(None, max_length=5)  # Query parameter for additional filtering
):
    return { "user": users[id], "query": q }  # Return user data with optional query parameter
