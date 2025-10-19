import telebot
from telebot import types

# оставь свой актуальный токен
TOKEN = "8440683490:AAGkb_Q9LIvofjMrFw9RmAFocRzTPh-2rkg"
bot = telebot.TeleBot(TOKEN)

CHANNEL_LINK = "https://t.me/cremestudio"

def channel_button():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("✨ В Crème Studio", url=CHANNEL_LINK))
    return markup

WELCOME_TEXT = (
    "Привет, {name} 🤍\n"
    "Crème Studio — пространство для тех, кто хочет расти в кондитерстве "
    "и вдохновляться каждый день ✨"
)

# 1) Красивое приветствие по /start
@bot.message_handler(commands=['start'])
def on_start(message):
    name = message.from_user.first_name or "друг"
    bot.send_message(
        message.chat.id,
        WELCOME_TEXT.format(name=name),
        reply_markup=channel_button()
    )

# 2) Команда /link — если попросят ссылку напрямую
@bot.message_handler(commands=['link', 'channel'])
def on_link(message):
    bot.send_message(message.chat.id, "Вот вход в мой канал:", reply_markup=channel_button())

# 3) Ответ на любые другие сообщения (чтобы всегда давать кнопку)
@bot.message_handler(func=lambda m: True)
def on_any_message(message):
    name = message.from_user.first_name or "друг"
    bot.reply_to(
        message,
        WELCOME_TEXT.format(name=name),
        reply_markup=channel_button()
    )

# запуск
bot.polling(none_stop=True)