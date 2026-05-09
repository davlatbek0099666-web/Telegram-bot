import telebot

TOKEN = "8670757219:AAHaGPc4yQpet7Wk_XV73mqgbOXrzL1C1Co"

bot = telebot.TeleBot(TOKEN)

# ADMIN ID
ADMIN_ID = 8670757219

# Userlar
users = set()


# START
@bot.message_handler(commands=['start'])
def start(message):

    users.add(message.chat.id)

    bot.send_message(
        message.chat.id,
        "Salom 😎\n\nMana havola:\nhttps://t.me/oyin_tic_tac_bot/tictactoe"
    )


# ADMIN PANEL
@bot.message_handler(commands=['admin'])
def admin_panel(message):

    if message.chat.id != ADMIN_ID:
        bot.reply_to(message, "Siz admin emassiz ❌")
        return

    bot.send_message(
        message.chat.id,
        f"""
👑 Admin Panel

👥 Userlar soni: {len(users)}

Komandalar:

/users - Userlar soni
/send xabar - Hammaga xabar
"""
    )


# USERLAR SONI
@bot.message_handler(commands=['users'])
def users_count(message):

    if message.chat.id != ADMIN_ID:
        return

    bot.send_message(
        message.chat.id,
        f"👥 Userlar soni: {len(users)}"
    )


# HAMMAGA XABAR
@bot.message_handler(commands=['send'])
def send_all(message):

    if message.chat.id != ADMIN_ID:
        return

    text = message.text.replace("/send ", "")

    for user in users:
        try:
            bot.send_message(user, text)
        except:
            pass

    bot.send_message(
        message.chat.id,
        "✅ Xabar yuborildi"
    )


print("Bot ishladi 🔥")

bot.infinity_polling()￼Enter
