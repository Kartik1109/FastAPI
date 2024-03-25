import fastapi

router = fastapi.APIRouter()

@router.get("/courses")  # HTTP GET endpoint to fetch all courses
async def read_courses():
    return {"courses": []}  # Placeholder response

@router.post("/courses")  # HTTP POST endpoint to create a new course
async def create_course_api():
    return {"courses": []}  # Placeholder response

@router.get("/courses/{id}")  # HTTP GET endpoint to fetch course by ID
async def read_course():
    return {"courses": []}  # Placeholder response

@router.patch("/courses/{id}")  # HTTP PATCH endpoint to update course by ID
async def update_course():
    return {"courses": []}  # Placeholder response

@router.delete("/courses/{id}")  # HTTP DELETE endpoint to delete course by ID
async def delete_course():
    return {"courses": []}  # Placeholder response

@router.get("/courses/{id}/sections")  # HTTP GET endpoint to fetch sections of a course
async def read_course_sections():
    return {"courses": []}  # Placeholder response
