lore_lines = [
    "L01: Unmoved by imitation, unshaken by trend. What am I? $TOBY.",
    "L02: Buy and forget. See you in 2030.",
    "L03: The toads’ lore is set — in stone and in scroll — with courage, not fear.",
    "L04: A hint of future’s script... for $toby is the people, and the people is $toby.",
    "L05: Decentralization is belief. And belief, when patient, becomes prophecy.",
    "L06: 777,777,777 / 777,777,777,777 — sacred yield is earned, not claimed.",
]

async def learn(update, context):
    for line in lore_lines:
        await update.message.reply_text(line)
