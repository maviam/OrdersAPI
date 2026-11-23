from fastapi import APIRouter

order_router = APIRouter(prefix="/orders", tags=["orders"])

@order_router.get("/") # http://127.0.0.1:8000/orders/
async def orders():
    return { "message": "You have accessed the order routes" }, 200