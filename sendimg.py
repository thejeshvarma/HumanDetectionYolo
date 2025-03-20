from telegram import Bot
import asyncio

# Replace with your bot token
BOT_TOKEN = "Bot TOken"

# Replace with the user's chat ID
CHAT_ID = "Chat id"

async def send_photo(image_path, chat_id=CHAT_ID):
    """Send a custom image via Telegram bot."""
    bot = Bot(token=BOT_TOKEN)
    with open(image_path, "rb") as image_file:
        await bot.send_photo(chat_id=chat_id, photo=image_file)
    print(f"Image '{image_path}' sent successfully!")

async def send_message(message, chat_id=CHAT_ID):
    """Send a custom text message via Telegram bot."""
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=chat_id, text=message)
    print(f"Message '{message}' sent successfully!")
