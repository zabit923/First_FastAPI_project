import time

from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from fastapi_cache.decorator import cache
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis

from auth.auth_config import auth_backend
from auth.models import User
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate
from operations.router import router as router_operation
from tasks.router import router as router_tasks




app = FastAPI(title='Trading App')



fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(router_operation)
app.include_router(router_tasks)


@app.on_event("startup")
async def startup_event():
    redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


