import telebot
import config
from telebot import TeleBot
from telebot import types

channel = '@PricoTv'
admin = '591250245'
chan_id = '1309874416'

bot = telebot.TeleBot(config.token, parse_mode='html')

keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row('Qullanma', '👨🏻‍💻 Admin')

keyboard2 = types.InlineKeyboardMarkup()
btn = types.InlineKeyboardButton('👁‍🗨 Aloqa', url='https://t.me/Winchestor0608')
keyboard2.add(btn)


# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):


@bot.message_handler(commands=['start'])
def welcom(message):
	bot.send_message(message.chat.id,
					 "Salom <b>{0}</b>  bu bot kanallardagi postlaringizni kommentariyasin uzgartiriberadi.".format(
						 message.from_user.first_name), reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def talk(message):
	if message.text == 'Qullanma':
		bot.send_message(message.chat.id,
						 "Buning uchun botni kanalingizga qo'shib administratorlik huquqlarini berib qo'yishingiz kerak!\n\n<code>#comment</code> va so'z - Har bir postingizga #comment so'zidan keyingi yozgan so'zingiz qo'shiladi\n<code>#text</code> - #comment ga yozlilgan matningiz\n<code>#clear</code> - #comment matnini o'chirib yuborish\n\n<b>Yuqorida keltirilgan buyruqlar faqat kanallarda ishlaydi!</b>")
	# \n<code>#text</code> - #comment ga yozlilgan matningiz\n<code>#clear</code> - #comment matnini o'chirib yuborish\n\n<b>Yuqorida keltirilgan buyruqlar faqat kanallarda ishlaydi!")
	elif message.text == '👨🏻‍💻 Admin':
		bot.send_message(message.chat.id, '<b>Dasturchi:</b> <em>Winchestor</em>*', reply_markup=keyboard2)


@bot.channel_post_handler(content_types=['text'])
def post(message):
	bot.edit_message_text(chat_id='@PricoTv', message_id=message.message_id,
						  text=str(message.text) + '\n\n▪️Biz @PricoTv ▪️damiz 👈 <b>QUSHILING❗️</b>')


@bot.channel_post_handler(content_types=['video', 'photo'])
def post_change(message):
	bot.edit_message_caption(chat_id='@PricoTv', message_id=message.message_id,
							 caption=str(message.caption) + '\n\n▪️Biz @PricoTv ▪️damiz 👈 <b>QUSHILING❗️</b>')


# menu_remove=types.ReplyKeyboardRemove()
bot.polling(none_stop=True)
