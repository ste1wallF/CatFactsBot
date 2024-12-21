import telebot
import requests

# Замените 'YOUR_API_TOKEN' на ваш реальный токен API от BotFather
API_TOKEN = '7648630895:AAE30Z-q4p3N5RWS3ut1uDJmXIctutgAcCk'

# Создаем экземпляр бота
bot = telebot.TeleBot(API_TOKEN)

# Функция для получения случайного факта о кошках
def get_cat_fact():
    response = requests.get('https://catfact.ninja/fact')
    if response.status_code == 200:
        fact = response.json()
        return fact['fact']
    else:
        return "Не удалось получить факт о кошках. Попробуйте позже."

# Обработчик команд /start и /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот, который отправляет случайные факты о кошках. Отправьте команду /catfact, чтобы получить факт.")

# Обработчик команды /catfact
@bot.message_handler(commands=['catfact'])
def send_cat_fact(message):
    fact = get_cat_fact()
    bot.reply_to(message, fact)

# Запускаем бота
bot.infinity_polling()
