#!/bin/bash

echo "Waiting Selenium..."
until $(curl --output /dev/null --silent --head --fail http://localhost:4444); do
    echo "Still waiting..."
    sleep 1
done

