from telegram.ext import ApplicationBuilder, CommandHandler
from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Следуйте по этой ссылке: https://account-oblivion-portal.lovable.app/")

if __name__ == '__main__':
    from os import getenv
    import logging

    logging.basicConfig(level=logging.INFO)

    application = ApplicationBuilder().token(getenv("BOT_TOKEN")).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()
