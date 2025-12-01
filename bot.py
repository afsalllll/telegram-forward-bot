from pyrogram import Client, filters
import asyncio
from config import API_ID, API_HASH, BOT_TOKEN, SOURCE_CHAT, TARGET_CHATS, SCHEDULE_TEXT, SCHEDULE_INTERVAL

app = Client(
    "forward-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Auto-forwarding
@app.on_message(filters.chat(SOURCE_CHAT))
async def forward(client, message):
    for chat in TARGET_CHATS:
        try:
            await message.copy(chat)
        except Exception as e:
            print(f"❌ Error sending to {chat}: {e}")

# Scheduled message
async def scheduled_task():
    while True:
        for chat in TARGET_CHATS:
            try:
                await app.send_message(chat, SCHEDULE_TEXT)
            except Exception as e:
                print(f"❌ Error sending scheduled message: {e}")
        await asyncio.sleep(SCHEDULE_INTERVAL)

@app.on_message(filters.command("start"))
async def start_msg(client, message):
    await message.reply("✅ Bot is running successfully!")

async def main():
    asyncio.create_task(scheduled_task())
    await app.start()
    print("Bot started!")
    await idle()

from pyrogram import idle

if __name__ == "__main__":
    app.run()
