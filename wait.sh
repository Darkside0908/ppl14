#!/bin/bash

echo "Waiting Selenium..."

until curl -s http://localhost:4444/wd/hub/status | grep -q "\"ready\":true"
do
    sleep 2
done

echo "Selenium Ready"