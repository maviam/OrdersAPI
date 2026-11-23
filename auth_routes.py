from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/") # http://127.0.0.1:8000/auth/
async def index():
    return { "message": "You have accessed the auth routes" }, 200