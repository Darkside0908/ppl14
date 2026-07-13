#!/bin/bash

echo "Waiting Selenium..."

until curl --silent http://localhost:4444/status | grep -q '"ready":true'
do
    sleep 2
done

echo "Selenium Ready"