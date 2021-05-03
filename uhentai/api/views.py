from .serializers import ChapterSerializer, GenreSerializer, SeriesSerializer
from .permissions import IsOwnerOrReadOnly
from core.models import Chapter, Genre, Series
from rest_framework import viewsets, permissions, mixins


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
		return serializer.save(owner=self.request.user)


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