import asyncio
import nest_asyncio
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackQueryHandler, ContextTypes

# Применяем nest_asyncio для предотвращения ошибок с закрытием событийного цикла
nest_asyncio.apply()

# Ваш токен, полученный от BotFather
TOKEN = "7809292354:AAFn2E9Rx5jmDgCplRRJcDVQ5MyuHN4Hp40"

# Ссылка или путь к видео
VIDEO_PATH = r"C:\\Users\\User\\Downloads\\1.mp4"  # Замените на путь к локальному видео

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Здравствуйте, как я могу к Вам обращаться?")

# Обработчик ответа с именем клиента
async def handle_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    client_name = update.message.text
    response = f'Приятно познакомиться, {client_name}. Меня зовут Светлана, нажми на видео чтобы узнать подробнее.'
    await update.message.reply_text(response)
    await send_video(update, context)

# Функция отправки видео
async def send_video(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Ссылка на видео вместо отправки файла
    video_url = "https://drive.google.com/file/d/1QuJePAW2DeOILdN3GwZJ8JmcUP2ugHpn/view?usp=drive_link"  # Замените на вашу ссылку на видео
    await update.message.reply_text(f"Посмотрите видео по ссылке: {video_url}")

    # Кнопка "Далее" добавляется сразу после ссылки на видео
    button = InlineKeyboardButton("Далее", callback_data='next')
    reply_markup = InlineKeyboardMarkup([[button]])
    await update.message.reply_text("После просмотра видео нажмите на кнопку 'Далее'", reply_markup=reply_markup)

# Обработчик нажатия кнопки "Далее"
async def button_next(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="Спасибо за просмотр! Вот второе видео для вас.")
    await query.message.reply_text("Посмотрите второе видео по ссылке: https://drive.google.com/file/d/1NODkr2lslELV55Zn3uyQbzZ6DZdXCIRJ/view?usp=drive_link")

    # Кнопки "Турист" и "Партнер"
    button_tourist = InlineKeyboardButton("Турист", callback_data='tourist')
    button_partner = InlineKeyboardButton("Партнер", callback_data='partner')
    reply_markup = InlineKeyboardMarkup([[button_tourist, button_partner]])
    await query.message.reply_text("Выберите, чтобы узнать подробнее:", reply_markup=reply_markup)

# Обработчики для кнопок "Турист" и "Партнер"
async def button_tourist(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="Вот видео для Туриста.")
    await query.message.reply_text("Посмотрите видео для клиента по ссылке: https://drive.google.com/file/d/1JZKS652uyKmIIrjIHFyYDNHdfZYh8wU_/view?usp=drive_link")

    # Кнопки "Регистрация" и "WhatsApp" для Туриста
    button_register = InlineKeyboardButton("Регистрация", url="https://sveta200296.incruises.com/")
    button_whatsapp = InlineKeyboardButton("WhatsApp", url="http://wa.me/77066804434")
    reply_markup = InlineKeyboardMarkup([[button_register, button_whatsapp]])
    await query.message.reply_text("Вы можете зарегистрироваться или связаться через WhatsApp:", reply_markup=reply_markup)

async def button_partner(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="Вот видео для Партнера.")
    await query.message.reply_text("Посмотрите видео для партнера по ссылке: https://drive.google.com/file/d/10OQBhpgqUCcwzItEXwdUP4sYFpO6HjHC/view?usp=drive_link")

    # Кнопки "Регистрация" и "WhatsApp" для Партнера
    button_register = InlineKeyboardButton("Регистрация", url="https://sveta200296.incruises.com/")
    button_whatsapp = InlineKeyboardButton("WhatsApp", url="http://wa.me/77066804434")
    reply_markup = InlineKeyboardMarkup([[button_register, button_whatsapp]])
    await query.message.reply_text("Вы можете зарегистрироваться или связаться через WhatsApp:", reply_markup=reply_markup)

# Основная функция, запускающая бота
async def main() -> None:
    # Создаем приложение и передаем ему токен вашего бота
    application = ApplicationBuilder().token(TOKEN).build()

    # Регистрируем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_name))
    application.add_handler(CallbackQueryHandler(button_next, pattern='next'))
    application.add_handler(CallbackQueryHandler(button_tourist, pattern='tourist'))
    application.add_handler(CallbackQueryHandler(button_partner, pattern='partner'))

    # Запуск бота
    await application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
