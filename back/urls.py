from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from .home import HomeAPIView
from django.conf.urls.static import static

urlpatterns = [
    path('',HomeAPIView.as_view()),
    path('admin/', admin.site.urls),
    path('users/',include('apps.app_users.urls')),
    path('images/',include('apps.app_images.urls')),
    path('videos/',include('apps.app_videos.urls')),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)