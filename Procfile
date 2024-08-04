release: python manage.py collectstatic --noinput
web: gunicorn YM.wsgi:application
worker: python manage.py runworker
