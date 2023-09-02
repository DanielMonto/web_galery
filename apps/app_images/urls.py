from django.urls import path
from .views import Images,ImageAPIView

urlpatterns=[
    path('',Images.as_view()),
    path('delete/<uuid:image_id>/',ImageAPIView.as_view())
]