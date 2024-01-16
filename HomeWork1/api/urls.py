from .views import *
from django.urls import path

urlpatterns = [
    path('', ProductGet.as_view()),
    path('<int:pk>', One.as_view()),
]
