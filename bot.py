import os
import asyncio

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers import start_handler

load_dotenv()


async def main():
    bot = Bot(token=os.environ.get("TOKEN"))
    dp = Dispatcher()
    
    dp.include_router(start_handler.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
