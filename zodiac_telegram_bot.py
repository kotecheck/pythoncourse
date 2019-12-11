from telebot import Telebot, types
import zodiac as z

bot = Telebot('ENTER_CODE')

@bot.message_handler(content_types=[ 'text'])
def get_text_message(message):
    if message.text == r'\hello':
        bot.send_message(message.from_user.id, 'Привет, сейчас я расскажу твой гороскопэ)