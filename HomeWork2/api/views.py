from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

# Create your views here.
class FilmGetList(ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class FilmRUD(RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class DirectorGetList(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class DirectorRUD(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer



class StyleGetList(ListCreateAPIView):
    queryset = Style.objects.all()
    serializer_class = StyleSerializer

class StyleRUD(RetrieveUpdateDestroyAPIView):
    queryset = Style.objects.all()
    serializer_class = StyleSerializer


class PosterGetList(ListCreateAPIView):
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer

class PosterRUD(RetrieveUpdateDestroyAPIView):
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer

