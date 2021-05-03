from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GenreViewSet, SeriesViewSet, ChapterViewSet


router = DefaultRouter()
router.register(r'g', GenreViewSet)
router.register(r's', SeriesViewSet)
router.register(r'c', ChapterViewSet)


urlpatterns = [
	path('', include(router.urls)),
	path('a/', include('rest_framework.urls', namespace='rest_framework'))
]