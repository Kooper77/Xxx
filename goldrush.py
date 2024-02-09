from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime, timedelta
import telebot
import time
import random

api_key = "6901951085:AAG2Sg1UN_ypJTKu51acxMGuxf8MCfdXWps"
user_id = '-1001785997071' 

bot = telebot.TeleBot(token=api_key)
link_instagram = '[ENTRE NO JOGO AQUI](https://google.com/)'


def send_sinal(hora):
    na = random.randint(5, 7)
    print("Sinal enviado...")
    bot.send_message(chat_id=user_id, text=(f'''
✅ *OPORTUNIDADE INDENTIFICADA*

🎮 *GOLD🌵RUSH*
🎰 Nª de Rodadas: {na}
⏰ Válido até: {hora}

🔥 '''f'{link_instagram}'''' 🔥


'''), parse_mode='MarkdownV2', disable_web_page_preview=True)
    return


while True:
    ha = datetime.now()
    na = random.randint(5, 7)
    ta = timedelta(minutes=na)
    nh = ha + ta
    nh = nh.strftime('%H:%M')
    send_sinal(nh)
    while True:
        hc = datetime.now().strftime('%H:%M')
        if hc == nh:
            bot.send_message(chat_id=user_id, text=(f'''✅✅✅ GREENN ✅✅✅'''))
            na = random.randint(2, 4)
            time.sleep(na)
            break
