from django.urls import path
from . import views

app_name = 'studyeng'
urlpatterns = [
    path('categories/', views.CategoryView.as_view(), name='categories'),
    path('themes/', views.ThemeView.as_view(), name='themes'),
    path('levels/', views.LevelView.as_view(), name='levels'),
    path('themes/<int:theme_id>',
         views.ThemeIDView.as_view(), name='themeids'),
    path('words/<int:theme_id>',
         views.WordIDView.as_view(), name='wordsids')
]