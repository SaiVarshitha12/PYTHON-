import telebot

BOT_TOKEN = '  # Direct use of token'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f"Hello, {message.chat.first_name}! Neenu confirm kosam chesthunna")

print("🤖 Bot is running... Press Ctrl+C to stop.")
bot.infinity_polling()
