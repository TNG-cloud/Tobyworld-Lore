from telegram import Update
from telegram.ext import ContextTypes

async def learn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Here is some Toadgod lore...")
