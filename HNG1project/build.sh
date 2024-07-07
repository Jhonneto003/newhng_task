#!/bin/bash

# Exit on error
set -e

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate