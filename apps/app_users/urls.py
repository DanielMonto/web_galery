from django.urls import path
from .views import MyTokenObtainPairView,Users
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns=[
    path('',Users.as_view()),
    path('login/',MyTokenObtainPairView.as_view()),
    path('refresh/',TokenRefreshView.as_view())
]