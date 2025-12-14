import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import json

# Telegram Bot Token
TOKEN = "8486043863:AAH8JiiRfD89_xJuQtLLGMpK4FIgk2LroVY"

# Logging configuration
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# API Mapping
API_MAP = {
    'cdn': 'https://pbx1botapi.vercel.app/api/hubcdn',
    'eflix': 'https://pbx1botapi.vercel.app/api/extraflix',
    'elink': 'https://pbx1botapi.vercel.app/api/extralink',
    'gd': 'https://pbx1botapi.vercel.app/api/driveleech',
    'gdr': 'https://pbx1botapi.vercel.app/api/gdrex',
    'ged': 'https://pbx1botapi.vercel.app/api/gdflix',
    'hb': 'https://pbx1botsapi2.vercel.app/api/hblinks',
    'hub': 'https://pbx1botapi.vercel.app/api/hubcloud',
    'lux': 'https://pbx1botapi.vercel.app/api/luxdrive',
    'neo': 'https://pbx1botapi.vercel.app/api/neo',
    'nex': 'https://pbx1botsapi2.vercel.app/api/nexdrive',
    'pcdn': 'https://pbx1botapi.vercel.app/api/pixelcdn',
    'seed': 'https://pbx1botapi.vercel.app/api/hubdrive',
    'vcl': 'https://pbx1botapi.vercel.app/api/vcloud',
    'vega': 'https://pbx1botsapi2.vercel.app/api/vega',
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sends a welcome message with available commands."""
    commands_list = "\n".join([f"/{cmd}" for cmd in sorted(API_MAP.keys())])
    welcome_text = (
        "Welcome to the Link Bypass Bot!\n\n"
        "Available commands:\n"
        f"{commands_list}\n\n"
        "Usage: /command <url>"
    )
    await update.message.reply_text(welcome_text)

async def handle_bypass(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles the bypass command by calling the corresponding API."""
    if not context.args:
        await update.message.reply_text("Please provide a URL after the command. Usage: /command <url>")
        return

    url = context.args[0]
    cmd = update.message.text.split()[0][1:]
    if '@' in cmd:
        cmd = cmd.split('@')[0]

    api_url = API_MAP.get(cmd)

    if not api_url:
        await update.message.reply_text("Unknown command.")
        return

    try:
        full_url = f"{api_url}?url={url}"
        response = requests.get(full_url)

        try:
            data = response.json()
            formatted_json = json.dumps(data, indent=2)
            if len(formatted_json) > 4000:
                formatted_json = formatted_json[:4000] + "..."

            await update.message.reply_text(f"```json\n{formatted_json}\n```", parse_mode='Markdown')
        except ValueError:
            await update.message.reply_text(response.text)

    except Exception as e:
        logging.error(f"Error processing {cmd}: {e}")
        await update.message.reply_text(f"Error occurred: {str(e)}")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    for cmd in API_MAP.keys():
        application.add_handler(CommandHandler(cmd, handle_bypass))

    print("Bot is polling...")
    application.run_polling()
