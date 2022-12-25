from django.urls import path
from . import views
app_name = 'base'
urlpatterns = [
    path('', views.home, name='home' ),
    path('add_room/', views.add_room, name='add_room'),
    path('delete_room/<int:id>/', views.delete_room, name='delete_room'),
    path('edit_room/<int:id>/', views.edit_room, name='edit_room'),
    path('room/<int:id>/', views.room, name='room'),
    path('delete_message/<int:id>/', views.delete_message, name='delete_message'),
]