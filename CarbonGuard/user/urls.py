from django.urls import path
from .views import UserListView, UserDetailView
from . import views

urlpatterns = [
    path('login/', views.login, name='user-login'),
    path('list/', UserListView.as_view(), name='user-list'),
    path('details/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('logout/', views.logout_view, name='logout')
]
