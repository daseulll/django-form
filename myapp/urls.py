from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('new/', views.post_new, name='post_new'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:post_pk>/comment/new/', views.comment_new, name='comment_new'),
]