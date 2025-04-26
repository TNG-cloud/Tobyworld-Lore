from telegram import Update
from telegram.ext import ContextTypes

async def poem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "In a realm where toads leap free,\n"
        "The Lore whispers through eternity.\n"
        "Study, believe, and walk with might,\n"
        "In patience and in light."
    )
