from fastapi import APIRouter

order_router  = APIRouter(
    prefix = "/order"
)

@order_router.get('/')
async def get_data(): 
    return {"message": "this is order router"}