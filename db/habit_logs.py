import asyncpg
from logger import logger
from datetime import date as DateType

async def log_habit(pool: asyncpg.Pool, habit_id: int, date: DateType) -> None:
    try:
        async with pool.acquire() as conn:
            await conn.execute("INSERT INTO habit_logs (habit_id, date) VALUES ($1, $2) ON CONFLICT DO NOTHING",
                habit_id, date)

    except Exception as e:
        logger.error(f"Error logging habit: {e}")
        raise


async def is_logged_today(pool: asyncpg.Pool, habit_id: int, date: DateType) -> bool:
    try:
        async with pool.acquire() as conn:
            return await conn.fetchval("SELECT EXISTS(SELECT 1 FROM habit_logs WHERE habit_id = $1 AND date = $2)",
                habit_id, date)
    except Exception as e:
        logger.error(f"Error getting habit log today: {e}")
        raise


async def get_habit_stats(pool: asyncpg.Pool, habit_id: int, days: int = 7) -> int:
    try:
        async with pool.acquire() as conn:
            return await conn.fetchval('''
                SELECT COUNT(*) FROM habit_logs
                WHERE habit_id = $1
                AND date >= CURRENT_DATE - $2
                ''', habit_id, days)
    except Exception as e:
        logger.error(f"Error getting count of habits on week: {e}")
        raise
