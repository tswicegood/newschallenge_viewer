web: python project/manage.py collectstatic --noinput ; python project/manage.py run_gunicorn -b "0.0.0.0:$PORT" -w 3
worker: python project/manage.py celeryd -c 2 -E -B --loglevel=INFO
