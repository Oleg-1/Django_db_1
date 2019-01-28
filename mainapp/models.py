from django.db import models


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    logo = models.ImageField(upload_to='departments', verbose_name='Логотип', blank=True)


class Person(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')  # varchar(30)
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    age = models.PositiveIntegerField(verbose_name='Возраст', default=0)

    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.last_name}"
