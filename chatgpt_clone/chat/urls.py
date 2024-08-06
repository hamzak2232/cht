from django.urls import path
from .views import send_message
from . import views


urlpatterns = [
    path('', views.chat_view, name='chat_view'),
    path('send_message/', views.send_message, name='send_message'),
    path('upload_file/', views.upload_file, name='upload_file'),
]
