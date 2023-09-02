from rest_framework.views import APIView
from .models import Video
from rest_framework_simplejwt.tokens import AccessToken
from django.http import HttpRequest
from ..app_users.models import UserOwn
from .serializers import VideoSerializer
from rest_framework import status
from rest_framework.response import Response

class Videos(APIView):
    def get(self,request:HttpRequest):
        user_id=AccessToken(request.META['HTTP_AUTHORIZATION'].split(' ')[1]).payload['user']['id']
        user=UserOwn.objects.get(id=user_id)
        images=Video.objects.filter(user=user)
        serializer=VideoSerializer(images,many=True)
        return Response(serializer.data)
    def post(self, request:HttpRequest):
        user_id=AccessToken(request.META['HTTP_AUTHORIZATION'].split(' ')[1]).payload['user']['id']
        user = UserOwn.objects.get(id=user_id)
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VideoAPIView(APIView):
    def delete(self,request,video_id):
        video=Video.objects.get(id=video_id)
        video.delete()
        return Response({'video':[video,'was deleted']},status=status.HTTP_200_OK)