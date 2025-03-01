from telethon import TelegramClient
import os

# Отримуємо змінні з GitHub Secrets
API_ID = os.getenv("API_ID")
if not API_ID:
    raise ValueError("API_ID не отримано!")

API_ID = int(API_ID)
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
USER_ID = os.getenv("USER_ID")
if not USER_ID:
    raise ValueError("USER_ID не отримано!")

USER_ID = int(USER_ID)

# Використовуємо MemorySession замість файлу сесії
bot = TelegramClient("MemorySession", API_ID, API_HASH).start(bot_token=BOT_TOKEN)

async def main():
    await bot.send_message(USER_ID, "✅ Бот запущено через GitHub Actions!")

with bot:
    bot.loop.run_until_complete(main())

print(f"DEBUG: API_ID={os.getenv('API_ID')}, API_HASH={os.getenv('API_HASH')}, BOT_TOKEN={os.getenv('BOT_TOKEN')}, USER_ID={os.getenv('USER_ID')}")

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

