#!/bin/bash

x=$((RANDOM % 101))  # Generate a random number between 0 and 100

if [ $x -lt 20 ]; then
    echo "Battery low! Return to base!"
    exit 1
fi

# Ping google.com (send 1 packet, wait max 2 sec, discard output)
if ! ping -c 1 -W 2 google.com > /dev/null 2>&1; then
    echo "Communication failure!"
    exit 1
fi

echo "All systems operational!"