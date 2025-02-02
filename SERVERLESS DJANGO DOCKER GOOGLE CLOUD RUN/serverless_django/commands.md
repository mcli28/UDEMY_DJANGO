
Production

python manage.py migrate --settings serverless_django.settings.production
python manage.py runserver --settings serverless_django.settings.production

DJANGO_SETTINGS_MODULE=serverless_django.settings.production waitress-serve serverless_django.wsgi:application