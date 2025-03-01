from telethon import TelegramClient
import os

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
USER_ID = os.getenv("USER_ID")

bot = TelegramClient("bot_session", API_ID, API_HASH).start(bot_token=BOT_TOKEN)
print(f"DEBUG: API_ID={API_ID}, API_HASH={API_HASH}, BOT_TOKEN={BOT_TOKEN}, USER_ID={USER_ID}")

if not API_ID or not API_HASH:
    raise ValueError("Помилка! API_ID або API_HASH не отримано!")

API_ID = int(API_ID)
USER_ID = int(USER_ID) if USER_ID else None

# 🔹 Ключові слова для пошуку
KEYWORDS = ["робота", "вакансія", "зустріч", "вечірка", "концерт", "місце", "час"]

# 🔹 Підключення до Telegram через бот-токен
bot = TelegramClient("bot_session", API_ID, API_HASH)
bot.start(bot_token=BOT_TOKEN)

# 📩 Відстежуємо нові повідомлення в групах і каналах
@bot.on(events.NewMessage)
async def handler(event):
    message_text = event.message.text.lower()  # Отримуємо текст повідомлення
    
    # 🔎 Перевіряємо, чи є ключові слова в повідомленні
    if any(word in message_text for word in KEYWORDS):
        print(f"🔹 Знайдено важливе повідомлення: {event.message.text}")

        # 📤 Відправляємо знайдене повідомлення у приватний чат (тобі)
        await bot.send_message(USER_ID, f"🔹 Важливе повідомлення: {event.message.text}")

# 🚀 Запускаємо бота
print("✅ Бот запущено. Чекаємо повідомлення...")
bot.run_until_disconnected()

