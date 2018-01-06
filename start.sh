#!/bin/bash

cd "$(dirname "$0")"

if ping -q -c 1 -W 1 8.8.8.8 >/dev/null; then
  echo "is online, try to pull new source"
  git pull
else
  echo is offline just run the app
fi

./windowed.py


