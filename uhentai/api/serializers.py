from rest_framework import serializers
from core.models import Genre, Chapter, Series


class GenreSerializer(serializers.ModelSerializer):
	class Meta:
		model = Genre
		fields = ['id', 'name']


class SeriesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Series
		fields = ['id', 'name', 'name_or', 'auth', 'owner']


class ChapterSerializer(serializers.ModelSerializer):
	class Meta:
		model = Chapter
		fields = ['id', 'name', 'number', 'series', 'genres', 'owner']