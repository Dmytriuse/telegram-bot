from telethon import TelegramClient, events

# 🔹 Введи свої дані
API_ID = 24347794  # Замінити на свій API ID
API_HASH = "6bafdcfbdd6267a40d7691743f51752c"  # Замінити на свій API Hash
BOT_TOKEN = "7998400388:AAGK9bAzGKu3NLeF36l5CWyuP50UD9s_RoY"  # Замінити на свій токен
USER_ID = 746698623  # ВСТАВ СВІЙ USER ID (знайдений через @userinfobot)

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

