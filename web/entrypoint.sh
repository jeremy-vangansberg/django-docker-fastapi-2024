#!/bin/sh

# Effectuer les migrations
echo "Effectuer les migrations de la base de données..."
python manage.py makemigrations && python manage.py migrate

# echo "Collect static files"
# python manage.py collectstatic --noinput

echo "Lancer le serveur"
# python manage.py runserver 0.0.0.0:80
gunicorn coinplon.wsgi:application --workers=4 --bind=0.0.0.0:80