from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.root, name='root'),
    path('recent/', views.recent, name='recent'),
    path('filter/', views.filter, name='filter'),
]
