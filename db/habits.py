import asyncpg
from logger import logger

async def add_habit(pool: asyncpg.Pool, user_id: int, title: str) -> int:
    try:
        async with pool.acquire() as conn:
            return await conn.fetchval("INSERT INTO habits (user_id, title) VALUES ($1, $2) RETURNING id",
            user_id, title)

    except Exception as e:
        logger.error(f"Error adding habit: {e}")
        raise


async def get_user_habits(pool: asyncpg.Pool, user_id: int) -> asyncpg.Record | None:
    try:
        async with pool.acquire() as conn:
            return await conn.fetch("SELECT id, title, created_at FROM habits WHERE user_id = $1", user_id)
    except Exception as e:
        logger.error(f"Error getting habit: {e}")
        raise


async def get_habit_by_id(pool: asyncpg.Pool, habit_id: int) -> asyncpg.Record | None:
    try:
        async with pool.acquire() as conn:
            return await conn.fetchrow("SELECT user_id, title, created_at FROM habits WHERE id = $1", habit_id)
    except Exception as e:
        logger.error(f"Error getting habit: {e}")
        raise


async def delete_habit(pool: asyncpg.Pool, habit_id: int) -> None:
    try:
        async with pool.acquire() as conn:
            await conn.execute("DELETE FROM habits WHERE id = $1", habit_id)
    except Exception as e:
        logger.error(f"Error delete habit: {e}")
        raise
