import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

async def ask(update, context):
    question = " ".join(context.args)
    if not question:
        await update.message.reply_text("Ask me something about the Lore.")
        return

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "system",
            "content": "You are the voice of Toadgod. Respond with clarity and poetic conviction about Tobyworld lore."
        }, {
            "role": "user",
            "content": question
        }]
    )

    await update.message.reply_text(response.choices[0].message.content.strip())
