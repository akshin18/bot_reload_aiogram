#!/bin/bash
set -e

echo "🔄 Stopping and removing existing containers..."
docker-compose down

echo "🏗️ Building and starting containers with force recreation..."
docker-compose up -d --force-recreate --build

echo "✅ Containers started successfully!"
docker-compose ps