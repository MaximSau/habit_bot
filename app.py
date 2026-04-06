from aiogram import Dispatcher, Bot
import db
from config.config import Config
import logger
import asyncio

async def main():
    config = Config()
    logger.setup_logger(config)
    pool = await db.create_pool(config)
    await db.init_db(pool)
    bot = Bot(config.bot_token)
    dp = Dispatcher()
    dp.workflow_data.update({'pool': pool, 'config': config})
    #TODO: зарегать хэндлеры
    try:
        await dp.start_polling(bot)
        logger.logger.info("Bot starting...")
    finally:
        logger.logger.error("Bot down")
        await pool.close()



if __name__ == '__main__':
    asyncio.run(main())
