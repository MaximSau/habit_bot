import asyncpg
from config.config import Config
from logger import logger


async def create_pool(config: Config) -> asyncpg.Pool:

    return await asyncpg.create_pool(
        user=config.db_user,
        password=config.db_password,
        database=config.db_name,
        host=config.db_host,
        port=config.db_port,
    )


async def init_db(pool: asyncpg.Pool) -> None:
    try:
        async with pool.acquire() as conn:
            await conn.execute('''
                CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                tg_id BIGINT UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT NOW()
                );
                ''')

            await conn.execute('''
                CREATE TABLE IF NOT EXISTS habits (
                id SERIAL PRIMARY KEY,
                user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
                title TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT NOW()
                )
                ''')

            await conn.execute('''
                CREATE TABLE IF NOT EXISTS habit_logs (
                id SERIAL PRIMARY KEY,
                habit_id INTEGER REFERENCES habits(id) ON DELETE CASCADE,
                date DATE NOT NULL,
                UNIQUE(habit_id, date)
                )
                ''')

    except Exception as e:
        logger.error(f"Error initializing database: {e}")
        raise
