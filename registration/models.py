from django.db import models

class User(models.Model):
    login = models.CharField('Логин', max_length=50)
    password = models.CharField('Пароль', max_length=50)
    name = models.CharField('Имя', max_length=50)
    second_name = models.CharField('Фамилия', max_length=50)
    name = models.CharField('Отчество', max_length=50)

# Create your models here.
