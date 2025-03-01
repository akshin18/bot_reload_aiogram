# Telegram Reload Bot

A Telegram bot built with aiogram that can execute a reload script on command.

## Features

- `/start` - Introduces the bot
- `/reload` - Executes a reload script and reports the results

## Setup with Docker Compose

### Prerequisites

- Docker and Docker Compose installed on your system
- A Telegram Bot Token (get one from [@BotFather](https://t.me/BotFather))

### Configuration

1. Copy the example environment file and add your Telegram Bot Token:

```bash
cp .env.example .env
```

2. Edit the `.env` file and add your Telegram Bot Token and external scripts path:

```
TELEGRAM_API_TOKEN=your_telegram_bot_token_here
EXTERNAL_SCRIPTS_PATH=/path/to/external/scripts
```

### Running the Bot

You can start the bot using the provided run script which will force recreation of containers:

```bash
chmod +x run.sh
./run.sh
```

Or manually with Docker Compose:

```bash
docker-compose up -d
```

### Viewing Logs

To see the bot's logs:

```bash
docker-compose logs -f
```

### Stopping the Bot

To stop the bot:

```bash
docker-compose down
```

## Development

If you want to run the bot without Docker for development:

1. Set up a Python virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -e .
```

3. Run the bot:

```bash
python main.py
```

## External Scripts

The bot is configured to access scripts from an external directory that is mounted as a volume in the Docker container. The path to this directory is specified in the `.env` file as `EXTERNAL_SCRIPTS_PATH`.

The bot expects to find the reload script at `/external_scripts/up.sh` inside the container. Make sure your external script is executable:

```bash
chmod +x /path/to/external/scripts/up.sh
```