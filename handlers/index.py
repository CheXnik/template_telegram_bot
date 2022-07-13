import logging

from aiogram import types
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from loader import dp, bot


logging.basicConfig(level=logging.INFO)
dp.middleware.setup(LoggingMiddleware())

# Хендлер для обычных функций
