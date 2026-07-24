from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from config import BOT_TOKEN


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌍 Welcome to Global Trade Network\n\n"
        "برای ثبت‌نام تاجر /register را بزنید."
    )


async def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    print("Bot is running...")

    await app.run_polling()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
