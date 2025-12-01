from pyrogram import Client, filters
import asyncio
import time

# ========================
# YOUR BOT CONFIG
# ========================
API_ID = 33300320
API_HASH = "49a2dd1e85164d95e77d9952a006c36b"
BOT_TOKEN = "8541239294:AAEsziaD5j-S30G-RhJt0iQDgq98RvX1tDM"

SOURCE_CHAT = -1003438376071   # your source channel

TARGET_CHATS = [
    -1002307923698,
    -1002738151866,
    -1002330208229,
    -1002583103466,
    -1002391657522,
    -1002306956966,
    -1002465666324,
    -1003445716234,
    -1002508347924
]

SCHEDULE_TEXT = "⏰ This is your scheduled message!"
SCHEDULE_INTERVAL = 3600  # 1 hour


# ========================
# START BOT
# ========================
app = Client(
    "forward-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


# ========================
# AUTO-FORWARD MESSAGES
# ========================
@app.on_message(filters.chat(SOURCE_CHAT))
async def auto_forward(client, message):
    for chat_id in TARGET_CHATS:
        try:
            await message.copy(chat_id)
            print(f"Forwarded to {chat_id}")
        except Exception as e:
            print(f"Error sending to {chat_id}: {e}")


# ========================
# SCHEDULED MESSAGE SENDER
# ========================
async def scheduled_sender():
    await app.start()
    while True:
        for chat_id in TARGET_CHATS:
            try:
                await app.send_message(chat_id, SCHEDULE_TEXT)
                print(f"Scheduled message sent to {chat_id}")
            except Exception as e:
                print(f"Error in scheduled msg to {chat_id}: {e}")

        await asyncio.sleep(SCHEDULE_INTERVAL)


# ========================
# RUN FOREVER
# ========================
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(scheduled_sender())
    app.run()
