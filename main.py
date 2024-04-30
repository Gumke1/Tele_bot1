import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import router
from data import db_session
from data.users import User
import requests
from aiogram import Bot, Dispatcher, types


async def main():
    db_session.global_init("db/blogs.db")
    bot = Bot(token="token")
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)



if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("off")
