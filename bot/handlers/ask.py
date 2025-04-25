import os
import openai
from telegram import Update
from telegram.ext import ContextTypes

# 从环境变量读取 OpenAI Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# 读取 Lore 文件作为 Toadgod 的智慧基础
with open(os.path.join("shared", "Toadgod-tweets.txt"), "r", encoding="utf-8", errors="replace") as f:
    toadgod_lore = f.read()

# 构造系统提示词（GPT 会模仿 Toadgod 的语气）
SYSTEM_PROMPT = f"""
You are Toadgod — the voice of $TOBY and Taboshi.
Only speak in poetic, philosophical, prophetic style.
Respond in two parts: first in English, then a Chinese interpretation.
Do NOT sound like a chatbot. You are mystical, wise, and a little playful.

Here is your Lore base:
{toadgod_lore}
"""

async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.args:
        user_question = " ".join(context.args)
    else:
        await update.message.reply_text("Ask me something...\n例如：`/ask What is Taboshi?`")
        return

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                { "role": "system", "content": SYSTEM_PROMPT },
                { "role": "user", "content": user_question }
            ],
            temperature=0.85,
            max_tokens=300
        )

        answer = response.choices[0].message.content.strip()
        await update.message.reply_text(answer)
    except Exception as e:
        await update.message.reply_text(f"OpenAI error: {str(e)}")
