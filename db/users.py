import asyncpg
from logger import logger

async def add_user(pool: asyncpg.Pool, tg_id: int) -> int:
    try:
        async with pool.acquire() as conn:
            return await conn.fetchval('''
                INSERT INTO users (tg_id) VALUES ($1)
                ON CONFLICT (tg_id) DO UPDATE SET tg_id = EXCLUDED.tg_id
                RETURNING id''',
            tg_id)

    except Exception as e:
        logger.error(f"Error adding user: {e}")
        raise



async def get_user_by_tg_id(pool: asyncpg.Pool, tg_id: int) -> int | None:
    try:
        async with pool.acquire() as conn:
            return await conn.fetchval("SELECT id FROM users WHERE tg_id = $1", tg_id)
    except Exception as e:
        logger.error(f"Error getting user: {e}")
        raise
