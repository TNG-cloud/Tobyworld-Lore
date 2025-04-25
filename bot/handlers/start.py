async def start(update, context):
    await update.message.reply_text(
        "Welcome to Lore Guardian.\nUse /learn or /ask to explore Toadgod's wisdom."
    )
