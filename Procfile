release: python YM/manage.py collectstatic --noinput
web: gunicorn YM.wsgi:application
worker: python YM/manage.py runworker
