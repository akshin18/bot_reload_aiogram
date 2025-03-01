FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    bash \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY pyproject.toml .
COPY main.py .

# Install Python dependencies
RUN pip install --no-cache-dir -e .

# Run the bot
CMD ["python", "main.py"]