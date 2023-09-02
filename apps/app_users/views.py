from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpRequest
from rest_framework.permissions import AllowAny
from .models import UserOwn
from django.contrib.auth.hashers import make_password
from .serializers import UserSerializer,MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.core.exceptions import ObjectDoesNotExist

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer
    def post(self,request:HttpRequest):
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            user = UserOwn.objects.get(username=username)
            if user.check_password(password):
                return super().post(request)
            else:
                return Response('contraseña incorrecta',status=400)
        except ObjectDoesNotExist:
            return Response('no existe el usuario',status=404)

class Users(APIView):
    permission_classes=[AllowAny]
    def get(self,request:HttpRequest):
        users=UserOwn.objects.all()
        serializer=UserSerializer(users,many=True).data
        return Response(serializer)
    def post(self,request:HttpRequest):
        try:
            user=UserOwn.objects.get(username=request.data['username'])
            return Response('nombre de usuario en uso',status=405)
        except ObjectDoesNotExist:
            user=UserOwn(username=request.data['username'],password=make_password(request.data['password']))
            user.save()
            serializer=UserSerializer(user,many=False)
            return Response(serializer.data)