import os
import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler
from handlers.start import start
from handlers.learn import learn
from handlers.ask import ask
from handlers.poem import poem

async def main():
    token = os.getenv("TELEGRAM_API_TOKEN")
    if not token:
        print("TELEGRAM_API_TOKEN not found in environment variables.")
        return

    application = ApplicationBuilder().token(token).build()

    # 添加命令处理器
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("learn", learn))
    application.add_handler(CommandHandler("ask", ask))
    application.add_handler(CommandHandler("poem", poem))

    print("Bot is running...")
    await application.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
