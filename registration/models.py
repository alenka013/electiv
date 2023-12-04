from django.db import models
from django.contrib.auth.models import AbstractUser

class Students(models.model):

class Facultets(models.model):
    code = models.CharField('Код',max_length=30)
    name = models.CharField('Направление подготовки',max_length=30)
    def __str__(self):
        return self.code

class Forms(models.model):
    name = models.CharField('Форма обучения',max_length=30)
    def __str__(self):
        return self.name

class Status(models.model):
    name = models.CharField('Статус',max_length=30)
    def __str__(self):
        return self.name

class Elective(models.model):
    name = models.CharField('Название', max_length=30)
    describe = models.CharField('Описание', max_length=255, null=True)
    id_froms = models.ForeignKey('Forms', on_delete=models.CASCADE)
    volume = models.IntegerField('Объем', max_length=3)
    date_start = models.DateField()
    date_finish = models.DateField()
    marks = models.FloatField('Минимальный балл', max_length=3)
    health = models.CharField('Предупреждение о здоровье', max_length=255)
    status = models.ForeignKey('Status', on_delete=models.CASCADE)

class e_f(models.model):
    id_elective = models.ForeignKey('Elective', on_delete=models.CASCADE)
    id_facultets = models.ForeignKey('Facultets', on_delete=models.CASCADE)
    year_study = models.IntegerField('Курс', max_length=1)

class e_s(models.model):
    id_elective = models.ForeignKey('Elective', on_delete=models.CASCADE)
    id_students = models.ForeignKey('Students', on_delete=models.CASCADE)
    year_study = models.IntegerField('Курс', max_length=1)


# Create your models here.
