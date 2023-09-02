from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import UserOwn

class UserSerializer(ModelSerializer):
    class Meta:
        model=UserOwn
        fields='__all__'
    
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user:UserOwn):
        token=super().get_token(user)
        token['user']={
            'id':str(user.id),
            'username':user.username,
            'files':user.files,
            'images':user.images,
            'is_staff':user.is_staff}
        return token