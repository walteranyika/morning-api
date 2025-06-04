from django.db import models

# Create your models here.
# pip install -r requirements.txt
class Person(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    edu_level = models.CharField(max_length=100)
    class Meta:
        db_table = 'watu'

# python manage.py makemigrations
# python manage.py migrate
# pip install django_rest_framework

# deepseek@ajiraemobilis.org
# @hublab!1


# python manage.py runserver




