from django.urls import path
from .views import Videos,VideoAPIView

urlpatterns=[
    path('',Videos.as_view()),
    path('delete/<uuid:video_id>/',VideoAPIView.as_view())
]