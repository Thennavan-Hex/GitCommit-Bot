import random
import string
import telebot
import test

token = "##############################################"  # Enter your telegram token

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "The Bot Start running...")


@bot.message_handler(commands=['commit'])
def send_welcome(message):
    file = open("E:\GitHub/2023/new.txt", "a")  # Enter Your text file
    N = 7

    res = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k=N))
    file.write(res)
    bot.reply_to(message, "commit added ")
    test.git_push()


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, """
	/start - Start the bot
	/commit - Commit today 
	/end - to close the bot""")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "The Given Command is not present try /help ")


bot.polling()

# designed by Source coders Junior developer  " Thens "
