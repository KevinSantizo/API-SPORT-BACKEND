web: gunicorn AppK.wsgi --log-file -
worker: celery -A config worker -l info --without-heartbeat
beat: celery -A config beat -S django