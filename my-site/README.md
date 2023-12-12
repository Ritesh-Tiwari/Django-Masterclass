# django_classes
This is my django framework class notes

# create virtual env 
cmd : python3 -m venv env_name

# activate env
cmd : source env_name/bin/activate

# install django
cmd : pip install django

# Creating a project in current folder ¶ 
cmd : django-admin startproject mysite .

# The development server¶
cmd : python manage.py runserver

# Creating the Food app¶
cmd  : python manage.py startapp food

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR /'static'
STATICFILES_DIRS = [
    'mysite/static',
]



# creating super user
cmd : python manage.py createsuperuser

username : admin
email_id : desiswag2024@gmail.com
password : admin
