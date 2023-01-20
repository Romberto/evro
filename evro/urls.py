from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.EvroView.as_view(), name='evro'),
    ]