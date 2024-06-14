from fastapi import APIRouter

auth_router = APIRouter(
    prefix = "/auth"
)

@auth_router.get('/')
async def get_data(): 
    return {"message": " welcome to auth routes"}
