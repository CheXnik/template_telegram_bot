import logging

from aiogram import types
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from data.config import ADMIN_ID
from loader import dp, bot


logging.basicConfig(level=logging.INFO)
dp.middleware.setup(LoggingMiddleware())

# Хендлер для функций администрирования
