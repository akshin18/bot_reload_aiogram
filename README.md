# Telegram Reload Bot

A Telegram bot built with aiogram that can execute a reload script on command.

## Features

- `/start` - Introduces the bot
- `/reload` - Executes a reload script and reports the results
- `/external` - Executes an external script from a different path

## Setup with Docker Compose

### Prerequisites

- Docker and Docker Compose installed on your system
- A Telegram Bot Token (get one from [@BotFather](https://t.me/BotFather))

### Configuration

1. Copy the example environment file and add your Telegram Bot Token:

```bash
cp .env.example .env
```

2. Edit the `.env` file and add your Telegram Bot Token and script paths:

```
TELEGRAM_API_TOKEN=your_telegram_bot_token_here
RELOAD_SCRIPT_PATH=/external_scripts/reload_script.sh
EXTERNAL_SCRIPT_PATH=/external_scripts/your_script.sh
```

3. Prepare your external scripts:
   - Create a directory for your external scripts (e.g., `/path/to/external/scripts`)
   - Add `reload_script.sh` and `your_script.sh` to this directory
   - Make sure both scripts are executable:
     ```bash
     chmod +x /path/to/external/scripts/*.sh
     ```

4. Update the `docker-compose.yml` file to mount your external scripts directory:

```yaml
volumes:
  # Mount the external scripts directory - update this path to your actual scripts location
  - /path/to/external/scripts:/external_scripts
```

### Script Requirements

- Both `reload_script.sh` and `your_script.sh` should be bash scripts
- Ensure the scripts have proper error handling and output
- Make the scripts executable with `chmod +x`

### Running the Bot

Start the bot using Docker Compose:

```bash
docker-compose up -d
```

This will build the Docker image and start the container in detached mode.

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

## Customizing the Reload Script

The reload script (`reload_script.sh`) is mounted as a volume in the Docker container. You can modify this script without rebuilding the container. Make sure the script is executable:

```bash
chmod +x reload_script.sh
```