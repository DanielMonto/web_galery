from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

urls = [
    {
        'apps': [
            {
                'app_users': [
                    {
                        'url': '/users/',
                        'description': 'for see and create users',
                        'methods': ['GET', 'POST']
                    },
                    {
                        'url': '/users/login/',
                        'description': 'for user login (obtain token)',
                        'methods': ['POST']
                    },
                    {
                        'url': '/users/refresh/',
                        'description': 'for token refresh',
                        'methods': ['POST']
                    }
                ]
            },
            {
                'app_videos': [
                    {
                        'url': '/videos/<uuid:video_id>/',
                        'description': 'get in their url from media and create videos with base64',
                        'methods': ['GET', 'POST']
                    },
                    {
                        'url': '/videos/delete/<uuid:video_id>/',
                        'description': 'delete videos',
                        'methods': ['DELETE']
                    }
                ]
            },
            {
                'app_images': [
                    {
                        'url': '/images/<uuid:image_id>/',
                        'description': 'get in their url from media and create images with base64',
                        'methods': ['GET', 'POST']
                    },
                    {
                        'url': '/images/delete/<uuid:image_id>/',
                        'description': 'delete images',
                        'methods': ['DELETE']
                    }
                ]
            }
        ]
    }
]

class HomeAPIView(APIView):
    permission_classes=[AllowAny]
    def get(self,request):
        return Response(urls)