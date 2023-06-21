from django.db import models

# Create your models here.

class Model(models.Model):
    objects = None
    name = models.CharField(max_length=20, help_text='Enter field documentation', default="some text", unique=True) #charfield - СТРОКА, max_length - длина объекта, 20 - макс кол-во символов
    number = models.PositiveSmallIntegerField(default=0)     # PositiveSmallIntegerField - поле для положительного маленького числа
    x = models.TextField() # в CharField длину указывать нужно, а в TextField может быть неограниченное кол-во символов
    # default - значение по умолчанию, unique - уникальность в случае с номерными знаками у машин

