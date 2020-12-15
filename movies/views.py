
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import MovieSerializer,MovieDBSerializer
from .models import Movie,Genre
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from knox.auth import TokenAuthentication
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
# Create your views here.

class MoviesView(ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = (IsAdminUser,)
    authentication_classes = (TokenAuthentication,)


class MovieSearch(generics.ListAPIView):
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    def get_queryset(self):
        qs=Movie.objects.all()
        name=self.request.GET.get('name')
        if name is not None:
           qs=qs.filter(Q(name__icontains=name)|Q(director__icontains=name)|Q(genre__name__icontains=name))
           #  qs = qs.filter(Q(name__icontains=name) | Q(director__icontains=name))

        return qs

class MovieDbSave(generics.CreateAPIView):
    serializer_class = MovieDBSerializer
    queryset = Movie.objects.all()
    permission_classes = (IsAdminUser,)
    authentication_classes = (TokenAuthentication,)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class MovieListView(generics.ListAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class MovieDeleteView(generics.DestroyAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    @action(detail=False, methods=['get'])
    def delete_all(self, request):
        Movie.objects.all().delete()
        return Response('success')
