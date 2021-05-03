from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Genre(models.Model):
	name = models.CharField(max_length=30, verbose_name='Назва жанру', unique=True)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name


class Series(models.Model):
	name = models.CharField(max_length=200, verbose_name='Назва серії')
	name_or = models.CharField(max_length=200, verbose_name='Назва мовою оригіналу', blank=True)
	auth = models.CharField(max_length=60, verbose_name='Автор', blank=True)
	owner = models.ForeignKey(User, models.DO_NOTHING, verbose_name='Власник')

	class Meta:
		ordering = ['-id']

	def __str__(self):
		return self.name


class Chapter(models.Model):
	name = models.CharField(max_length=200, verbose_name='Назва глави', blank=True)
	number = models.IntegerField('Порядковий номер в серії')
	series = models.ForeignKey(Series, models.CASCADE, verbose_name='Серія')
	owner = models.ForeignKey(User, models.DO_NOTHING, verbose_name='Власник')
	genres = models.ManyToManyField(Genre, verbose_name='Жанри')