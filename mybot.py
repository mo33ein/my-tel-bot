from telegram.ext import ApplicationBuilder, MessageHandler, filters, CommandHandler
from telegram import Update
from telegram.ext import ContextTypes

# شمارش پیام‌های پشت سر هم برای هر کاربر
user_message_counts = {}
last_user_id = None

# جملات هشداردهنده
warning_messages = [
    "ای بنازمت 😐 پشتکار فقط خودت و بس",
    "اوففف.قلبم ریخت.بگو و بیا 🤨",
    "رگبار شروع شد.سنگر بگیرید 😉",
"بعضی وقتا فکر میکنم فقط خودم رباتم 😅",
    "عشقم یکم آرومتر.قلبم وایساد 😅",
    "اوففف. سونامی اومد..پناه بگیرید 😅"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام عزیز دلم! من رباتتم 😎")

async def handle_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global last_user_id

    user_id = update.message.from_user.id

    # اگه کاربر همون قبلیه، شمارش +1
    if user_id == last_user_id:
        user_message_counts[user_id] = user_message_counts.get(user_id, 0) + 1
    else:
        # اگه کاربر جدید باشه، فقط شمارش اون یکی صفر شه
        user_message_counts[user_id] = 1
        last_user_id = user_id

    # اگه رسید به ۵ پیام پیاپی
    if user_message_counts[user_id] == 5:
        from random import choice
        await update.message.reply_text(choice(warning_messages))

if __name__ == '__main__':
    app = ApplicationBuilder().token("8075961087:AAGC0PBFbIbeogUKAZKXKQFQr9qayKKDVt8").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_messages))

    print("ربات روشنه عزیز دلم ❤️")
    app.run_polling()