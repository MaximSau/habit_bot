import asyncpg
from logger import logger

async def add_habit(pool: asyncpg.Pool, tg_id: int) -> int:
    return 1


async def get_user_habits(pool: asyncpg.Pool, user_id: int) -> tuple | None:
    pass


async def get_habit_by_id(pool: asyncpg.Pool, habit_id: int) -> tuple | None:
    pass


async def delete_habit(pool: asyncpg.Pool, habit_id: int) -> None:
    pass
