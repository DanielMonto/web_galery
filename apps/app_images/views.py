from rest_framework.views import APIView
from .models import Image
from apps.app_users.models import UserOwn
from rest_framework_simplejwt.tokens import AccessToken
from django.http import HttpRequest
from .serializers import ImageSerializer
from rest_framework import status
from rest_framework.response import Response

class Images(APIView):
    def get(self,request:HttpRequest):
        user_id=AccessToken(request.META['HTTP_AUTHORIZATION'].split(' ')[1]).payload['user']['id']
        user=UserOwn.objects.get(id=user_id)
        images=Image.objects.filter(user=user)
        serializer=ImageSerializer(images,many=True)
        return Response(serializer.data)
    def post(self, request:HttpRequest):
        user_id=AccessToken(request.META['HTTP_AUTHORIZATION'].split(' ')[1]).payload['user']['id']
        user = UserOwn.objects.get(id=user_id)
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ImageAPIView(APIView):
    def delete(self,request,image_id):
        image=Image.objects.get(id=image_id)
        image.delete()
        return Response({'Image':[image,'was deleted']},status=status.HTTP_200_OK)