#!/usr/bin/env bash

# go to script directory
cd "$(dirname "$0")"

# activate virtual environment
source venv/bin/activate

# run app
python ui.py
