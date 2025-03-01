import logging
import subprocess
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.enums import ParseMode
import asyncio
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Path to your bash scripts
RELOAD_SCRIPT = os.getenv("RELOAD_SCRIPT_PATH", "/external_scripts/up.sh")

def escape_markdown_v2(text):
    special_chars = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
    for char in special_chars:
        text = text.replace(char, f"\\{char}")
    return text

@dp.message(Command("reload"))
async def cmd_reload(message: types.Message):
    await message.answer("🔄 Starting reload process. Please wait...")

    try:
        process = subprocess.Popen(
            ["bash", RELOAD_SCRIPT],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        stdout, stderr = process.communicate()

        if process.returncode == 0:
            response = f"✅ Reload completed successfully!\n\n"
            if stdout.strip():
                escaped_stdout = escape_markdown_v2(stdout.strip())
                response += f"Output:\n```\n{escaped_stdout}\n```"
        else:
            response = f"❌ Reload failed with exit code {process.returncode}\\.\n\n"
            if stderr.strip():
                escaped_stderr = escape_markdown_v2(stderr.strip())
                response += f"Error:\n```\n{escaped_stderr}\n```"
            if stdout.strip():
                escaped_stdout = escape_markdown_v2(stdout.strip())
                response += f"\nOutput:\n```\n{escaped_stdout}\n```"

        await message.answer(response, parse_mode=ParseMode.MARKDOWN_V2)

    except Exception as e:
        await message.answer(f"❌ An error occurred: {str(e)}")

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    """Handler for the /start command"""
    await message.answer("Hello! I'm a bot that can reload your services.\n"
                         "Use /reload to restart the main service.\n"
                         "Use /tg_reload to restart the TG reactions service.")

async def main():
    # Start the bot
    await bot.delete_webhook(drop_pending_updates=True)
    # Start polling
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())