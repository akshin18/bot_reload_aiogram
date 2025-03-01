#!/bin/bash
set -e

# Clean up any existing containers with the same name
docker rm -f telegram-reload-bot 2>/dev/null || true

# Start the container
docker-compose up --build -d

# Show status
docker-compose ps