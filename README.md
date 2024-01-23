git clone git@github.com:Brenolima03/ecommerce.git

cd ecommerce

# Para Linux
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt

# Para Windows
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
