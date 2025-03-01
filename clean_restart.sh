#!/bin/bash
set -e

echo "Stopping any existing containers..."
docker-compose down || true

echo "Removing any existing containers with the same name..."
docker rm -f telegram-reload-bot 2>/dev/null || true

echo "Removing any dangling images..."
docker image prune -f

echo "Building and starting the container..."
docker-compose up --build -d

echo "Container status:"
docker-compose ps