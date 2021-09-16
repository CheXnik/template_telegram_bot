import logging

from aiogram.contrib.middlewares.logging import LoggingMiddleware

logging.basicConfig(level=logging.INFO)

from loader import dp

dp.middleware.setup(LoggingMiddleware())

# Хендлер для обычных функций
