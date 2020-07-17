from django.http import HttpResponse, Http404
from django.core.exceptions import PermissionDenied
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CategorySerializer, \
    ThemeSerializer, LevelSerializer, \
    WordSerializer, ThemeIDSerializer
from .models import Category, Theme, Level, Word
from django.conf import settings


class AuthenticationView(APIView):
    def check_API_secret(self, request):
        secret = request.META.get('HTTP_SECRET')
        if not (secret and
                secret == settings.API_SECRET):
            raise PermissionDenied("enter credentials")

class CategoryView(AuthenticationView):
    def get(self, request, *args, **kwargs):
        super().check_API_secret(request)
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True, context={"request":request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class ThemeView(AuthenticationView):
    def get(self, request, *args, **kwargs):
        super().check_API_secret(request)
        queryset = Theme.objects.all()
        serializer = ThemeSerializer(queryset, many=True, context={"request":request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class LevelView(AuthenticationView):
    def get(self, request, *args, **kwargs):
        super().check_API_secret(request)
        queryset = Level.objects.all()
        serializer = LevelSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ThemeIDView(AuthenticationView):
    def get(self, request, theme_id):
        super().check_API_secret(request)
        try:
            queryset = Theme.objects.get(id=theme_id)
        except Exception:
            raise Http404('тема не найдена')
        serializer = ThemeIDSerializer(queryset, context={"request":request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class WordIDView(AuthenticationView):
    def get(self, request, theme_id):
        super().check_API_secret(request)
        try:
            queryset = Word.objects.get(id=theme_id)
        except Exception:
            raise Http404('слово не найдено')
        serializer = WordSerializer(queryset, context={"request":request})
        return Response(serializer.data, status=status.HTTP_200_OK)