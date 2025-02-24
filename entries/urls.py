from django.urls import path
from . import views

urlpatterns = [
    path('', views.entry_list, name='entry_list'),
    path('create/', views.entry_create, name='entry_create'),
    path('<int:entry_id>/toggle-review/', views.toggle_review, name='toggle_review'),
    path('<int:entry_id>/', views.entry_detail, name='entry_detail'),
]