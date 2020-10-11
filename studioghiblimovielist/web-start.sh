ls
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py import_initial_data
python manage.py runserver 0.0.0.0:8000