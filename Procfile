release: python YM/manage.py --noinput
web: gunicorn YM.wsgi:application
worker: python YM/manage.py runworker
