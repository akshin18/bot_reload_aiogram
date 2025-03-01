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

@dp.message(Command("reload"))
async def cmd_reload(message: types.Message):
    """
    Handler for the /reload command.
    Executes a bash script and sends messages before and after execution.
    """
    # Check if the user has permission (optional)
    # allowed_user_ids = [123456789]  # Replace with your Telegram user ID
    # if message.from_user.id not in allowed_user_ids:
    #    await message.answer("You don't have permission to use this command.")
    #    return

    await message.answer("🔄 Starting reload process. Please wait...")

    try:
        # Execute the bash script
        process = subprocess.Popen(
            ["bash", RELOAD_SCRIPT],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        stdout, stderr = process.communicate()

        if process.returncode == 0:
            # Script executed successfully
            response = f"✅ Reload completed successfully!\n\n"
            if stdout.strip():
                response += f"Output:\n```\n{stdout.strip()}\n```"
        else:
            # Script execution failed
            response = f"❌ Reload failed with exit code {process.returncode}.\n\n"
            if stderr.strip():
                response += f"Error:\n```\n{stderr.strip()}\n```"
            if stdout.strip():
                response += f"\nOutput:\n```\n{stdout.strip()}\n```"

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