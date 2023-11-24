from django.urls import path
from . import views

app_name = 'cnn'

urlpatterns = [
    path('', views.page_cnn, name='page_cnn'),
]
