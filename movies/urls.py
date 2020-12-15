from django.urls import path, include
from rest_framework import routers
from .views import MoviesView,MovieSearch,MovieDbSave,MovieListView,MovieDeleteView

router = routers.DefaultRouter()
router.register(r'movie', MoviesView)
#router.register(r'moviesearch', MovieSearch)

urlpatterns = [
    path('moviecurd', include(router.urls)),
    path('api/search1/', MovieSearch.as_view()),
    path('moviedbsave/', MovieDbSave.as_view()),
    path('movielist/', MovieListView.as_view()),
    path('moviedelete/', MovieDeleteView.as_view())
 ]