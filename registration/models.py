from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):

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
    id_teachers = models.ForeignKey('Teachers', on_delete=models.CASCADE)
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
    marks = models.FloatField('Балл студента', max_length=3)

class e_t(models.model):
    id_elective = models.ForeignKey('Elective', on_delete=models.CASCADE)
    id_teachers = models.ForeignKey('Teachers', on_delete=models.CASCADE)

class Test(models.model):
    id_elective = models.ForeignKey('Elective', on_delete=models.CASCADE)
    title = models.CharField('Название', max_length=255, null=True)
    active = models.BooleanField('Активный')

class Questions(models.model):
    id_test = models.ForeignKey('Test', on_delete=models.CASCADE)
    text = models.CharField('Вопрос', max_length=255, null=True)
    image = models.URLField('Фото_вопроса', max_length=255, null=True)
    marks = models.IntegerField('Балл за вопрос', max_length=3, default=1)

class Option(models.model):
    id_questions = models.ForeignKey('Questions', on_delete=models.CASCADE)
    text = models.CharField('Вариант ответа', max_length=255, null=True)
    answer = models.BooleanField('Правильный ли?',default=False)




# Create your models here.
