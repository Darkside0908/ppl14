#!/bin/bash
set -uo pipefail

echo "Waiting for Selenium to be ready..."

MAX_ATTEMPTS=60
ATTEMPT=0

until curl -s http://localhost:4444/status | grep -q '"ready": *true'; do
    ATTEMPT=$((ATTEMPT + 1))
    if [ "$ATTEMPT" -ge "$MAX_ATTEMPTS" ]; then
        echo "Selenium did not become ready after $((MAX_ATTEMPTS * 2))s"
        echo "---- docker ps ----"
        docker ps -a
        echo "---- selenium logs ----"
        docker logs selenium || true
        exit 1
    fi
    echo "Still waiting... ($ATTEMPT/$MAX_ATTEMPTS)"
    sleep 2
done

echo "Selenium is ready."

