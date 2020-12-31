from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:text_id>/', views.detail, name='detail'),
]
