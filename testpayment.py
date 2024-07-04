from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext import filters


# 替换为你的 Bot 的 API Token
API_TOKEN = '7312590200:AAGmFaFKBuF54DA9DSHI6S4eLuueHGSW--E'

# 处理 /start 命令的函数
def start(update, context):
    update.message.reply_text('你好！我是你的第一个 Telegram Bot！')

# 处理用户发送的消息的函数
def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    # 创建 Updater 对象并传入 API Token
    updater = Updater(API_TOKEN, use_context=True)

    # 获取 Dispatcher 对象
    dp = updater.dispatcher

    # 添加处理 /start 命令的处理器
    dp.add_handler(CommandHandler("start", start))

    # 添加处理用户发送的消息的处理器
    dp.add_handler(MessageHandler(filters.text & ~filters.command, echo))

    # 开始接收和处理消息
    updater.start_polling()

    # 让程序保持运行，直到用户按 Ctrl-C 退出
    updater.idle()

if __name__ == '__main__':
    main()
