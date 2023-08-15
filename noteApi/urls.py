from django.urls import path
from . import views

urlpatterns = [
    # path('', views.reactView, name='view'),
    path('routes/', views.getRoutes, name='routes'),
    path('notes/', views.dbNotes, name='notes'),
    path('notes/create/', views.createNote, name='create-note'),
    path('notes/<str:pk>/', views.dbNote, name='note'),
    path('notes/<str:pk>/update/', views.updateNote, name='update-note'),
    path('notes/<str:pk>/delete/', views.deleteNote, name='delete-note')
]
