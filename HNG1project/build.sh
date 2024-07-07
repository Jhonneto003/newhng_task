#!/bin/bash

# Exit on error
set -e

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files
<<<<<<< HEAD
python manage.py collectstatic --noinput
=======
python manage.py collectstatic --noinput
>>>>>>> be2d73b028d36746c69ab0e6c30e5f13bc0a2ab5
