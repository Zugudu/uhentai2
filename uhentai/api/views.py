from .serializers import ChapterSerializer, GenreSerializer, SeriesSerializer
from .permissions import IsOwnerOrReadOnly
from core.models import Chapter, Genre, Series
from rest_framework import viewsets, permissions, mixins
from django.conf import settings
import os


# Create your views here.
class GenreViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Genre.objects.all()
	serializer_class = GenreSerializer


class SeriesViewSet(mixins.CreateModelMixin,
					mixins.ListModelMixin,
					mixins.RetrieveModelMixin,
					mixins.UpdateModelMixin,
					viewsets.GenericViewSet):
	queryset = Series.objects.all()
	serializer_class = SeriesSerializer
	permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly]

	def perform_create(self, serializer):
		series = serializer.save(owner=self.request.user)
		try:
			os.makedirs(os.path.join(settings.MEDIA_ROOT, str(series.id)))
		except OSError:
			series.delete()
			return (500, 'Can\'t create series')
		return series


class ChapterViewSet(mixins.CreateModelMixin,
					mixins.ListModelMixin,
					mixins.RetrieveModelMixin,
					mixins.UpdateModelMixin,
					viewsets.GenericViewSet):
	queryset = Chapter.objects.all()
	serializer_class = ChapterSerializer
	permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly]

	def perform_create(self, serializer):
		return serializer.save(owner=self.request.user)