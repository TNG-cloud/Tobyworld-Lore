from telegram import Update
from telegram.ext import ContextTypes
import openai
import os

async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question = " ".join(context.args)
    if not question:
        await update.message.reply_text("Please ask me a question about the Lore.")
        return

    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are the voice of Toadgod. Respond about Tobyworld lore with clarity and poetic wisdom."
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    await update.message.reply_text(response['choices'][0]['message']['content'])
