from aiogram import Router
from .start import start_router
from .habits import habits_router
from .stats import stats_router

# Главный роутер
main_router = Router()
main_router.include_router(start_router)
main_router.include_router(habits_router)
main_router.include_router(stats_router)
