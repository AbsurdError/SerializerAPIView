from .views import *
from django.urls import path

urlpatterns = [
    path('', FilmGetList.as_view()),
    path('<int:pk>', FilmGetList.as_view()),
    path('films-rud/<int:pk>', FilmRUD.as_view()),
    path('directors', DirectorGetList.as_view()),
    path('directors/<int:pk>', DirectorGetList.as_view()),
    path('direct-rud/<int:pk>', DirectorRUD.as_view()),
    path('styles', StyleGetList.as_view()),
    path('styles/<int:pk>', StyleGetList.as_view()),
    path('style-rud/<int:pk>', StyleRUD.as_view()),
    path('posters', PosterGetList.as_view()),
    path('posters/<int:pk>', PosterGetList.as_view()),
    path('poster-rud/<int:pk>', PosterRUD.as_view()),
]
