import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable is not set")

WELCOME_TEXT = (
    "Welcome to Dategram Club 👋\n\n"
    "Stay connected with the latest updates, content and community news.\n\n"
    "Choose an option below to get started."
)


def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Latest Updates", callback_data="updates")],
        [InlineKeyboardButton("Content", callback_data="content")],
        [InlineKeyboardButton("About", callback_data="about")],
    ])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_TEXT, reply_markup=main_menu())


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "updates":
        text = (
            "Latest Updates\n\n"
            "Keep an eye here for new posts, announcements and fresh content."
        )
    elif query.data == "content":
        text = (
            "Content\n\n"
            "This is where new photos, posts and other community content can be shared."
        )
    elif query.data == "about":
        text = (
            "About Dategram Club\n\n"
            "A simple community space for fans, updates and exclusive content."
        )
    else:
        text = WELCOME_TEXT

    await query.edit_message_text(text, reply_markup=main_menu())


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Use the buttons below to explore Dategram Club.",
        reply_markup=main_menu(),
    )


def run():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CallbackQueryHandler(buttons))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    run()
